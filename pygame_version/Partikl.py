# Klasa za robota koji ce ici po lavirintu i meriti
import pygame as pg
from pygame_version import parametri
from pygame_version.Laser import Laser
vec = pg.math.Vector2



class Partikl(pg.sprite.Sprite):
    def __init__(self, simulacija, x, y, rot):
        self.grupe = simulacija.svi_sprajtovi
        self.simulacija = simulacija
        self.crtaj_partikl = True

        pg.sprite.Sprite.__init__(self, self.grupe)

        self.original_image = pg.Surface((10, 10), pg.SRCALPHA)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rot_speed = 3
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = rot

        self.laser = Laser(self)
        self.laser.boja_lasera = parametri.CRNA

    def update(self):
        self.rot_speed = self.simulacija.robot.rot_speed
        self.vel = self.simulacija.robot.vel

        new_sprite = pg.sprite.Sprite()
        new_rect = pg.Rect(self.rect)
        new_rect.x += self.vel[0]
        new_rect.y += self.vel[1]
        new_sprite.rect = new_rect
        if pg.sprite.spritecollide(new_sprite, self.simulacija.lavirint_sprajtovi, False):
            self.vel = vec(0, 0)

        self.rot += self.rot_speed
        self.vel = self.vel.rotate(self.simulacija.robot.rot)
        self.vel = self.vel.rotate(-self.rot)
        self.pos += self.vel
        # self.image = pg.transform.rotate(self.original_image, self.rot)
        pg.draw.circle(self.image, parametri.SVETLO_SIVA, (5, 5), 5)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos
