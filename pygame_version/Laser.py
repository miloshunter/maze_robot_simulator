# Klasa za robota koji ce ici po lavirintu i meriti
import pygame as pg
from pygame_version import parametri
import copy
import math
vec = pg.math.Vector2



class Laser(pg.sprite.Sprite):
    def __init__(self, robot, ofset_pozicije_lasera):
        pg.sprite.Sprite.__init__(self, robot.simulacija.svi_sprajtovi)

        ATOM_IMG = pg.Surface((parametri.SIRINA, parametri.VISINA), pg.SRCALPHA)
        self.boja_lasera = parametri.CRVENA
        self.robot = robot
        self.simulacija = robot.simulacija
        self.image = ATOM_IMG
        self.rect = self.image.get_rect()
        self.merenje_lasera = parametri.DOMET_LASERA

        self.ofset_pozicije_lasera = ofset_pozicije_lasera

    def update(self):
        def rotate(x, y, xo, yo, theta):  # rotate x,y around xo,yo by theta (rad)
            xr = math.cos(theta) * (x - xo) - math.sin(theta) * (y - yo) + xo
            yr = math.sin(theta) * (x - xo) + math.cos(theta) * (y - yo) + yo
            return [xr, yr]

        razdaljina_od_centra = parametri.DUZINA_ROBOTA / 2
        pozicija1 = copy.deepcopy(self.robot.pos)
        # if self.ofset_pozicije_lasera[1] != 0:
        #     pozicija1[0] += self.ofset_pozicije_lasera[0]
        #     pozicija1[0], pozicija1[1] = rotate(pozicija1[0], pozicija1[1],
        #                                         self.robot.rect.center[0],
        #                                         self.robot.rect.center[1],
        #                                         -self.robot.rot * 3.14 / 180)
        pozicija2 = copy.deepcopy(self.robot.pos)
        pozicija2 += self.ofset_pozicije_lasera
        pozicija2[0], pozicija2[1] = rotate(pozicija2[0], pozicija2[1],
                                            self.robot.rect.center[0],
                                            self.robot.rect.center[1],
                                            -self.robot.rot*3.14/180)

        levo = min(pozicija1[0], pozicija2[0])
        desno = max(pozicija1[0], pozicija2[0])
        gore = min(pozicija1[1], pozicija2[1])
        dole = max(pozicija1[1], pozicija2[1])

        self.rect = pg.Rect(0, 0, parametri.SIRINA, parametri.VISINA)

        ATOM_IMG = pg.Surface((parametri.SIRINA, parametri.VISINA), pg.SRCALPHA)
        self.image = ATOM_IMG

        preseci_sa_zidovima = []

        for zid in self.simulacija.lavirint.zidovi:
            bottomleft = zid.rect.bottomleft
            bottomright = zid.rect.bottomright
            topleft = zid.rect.topleft
            topright = zid.rect.topright

            presek1 = self.measure_distance(pozicija1[0], pozicija1[1], pozicija2[0], pozicija2[1],
                                            topleft[0], topleft[1], topright[0], topright[1])
            if presek1:
                preseci_sa_zidovima.append(presek1)
            presek2 = self.measure_distance(pozicija1[0], pozicija1[1], pozicija2[0], pozicija2[1],
                                            bottomleft[0], bottomleft[1], bottomright[0], bottomright[1])
            if presek2:
                preseci_sa_zidovima.append(presek2)
            presek3 = self.measure_distance(pozicija1[0], pozicija1[1], pozicija2[0], pozicija2[1],
                                            topleft[0], topleft[1], bottomleft[0], bottomleft[1])
            if presek3:
                preseci_sa_zidovima.append(presek3)
            presek4 = self.measure_distance(pozicija1[0], pozicija1[1], pozicija2[0], pozicija2[1],
                                            bottomright[0], bottomright[1], topright[0], topright[1])
            if presek4:
                preseci_sa_zidovima.append(presek4)

        crtaj_do = pozicija2
        razdaljina = 200

        if any(preseci_sa_zidovima):
            # Nalazenje najblize tacke preseka
            new_list = [math.sqrt((self.robot.pos[0]-x[0])**2 + (self.robot.pos[1]-x[1])**2) for x in preseci_sa_zidovima]

            mn, idx = min((new_list[i], i) for i in range(len(new_list)))

            presek = preseci_sa_zidovima[idx]
            razdaljina = mn
            if presek:
                pg.draw.circle(self.image, parametri.CRVENA, (presek[0],
                                                              presek[1]),
                               3)
                crtaj_do = presek

        pg.draw.line(self.image, self.boja_lasera, pozicija1, crtaj_do)
        self.merenje_lasera = int(razdaljina)



    def measure_distance(self, x1, y1, x2, y2, x3, y3, x4, y4):
        def lineLine(x1, y1, x2, y2, x3, y3, x4, y4):
            #  Calculate direction of the lines
            try:
                uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) /\
                     ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
            except ZeroDivisionError:
                return 0
            try:
                uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) /\
                     ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
            except ZeroDivisionError:
                return 0

            if uA >= 0 and uA <=1 and uB >= 0 and uB <=1:
                intersectionX = int(x1 + (uA * (x2-x1)))
                intersectionY = int(y1 + (uA * (y2 - y1)))

                return intersectionX, intersectionY
            else:
                return None

        return lineLine(x1, y1, x2, y2, x3, y3, x4, y4)