# Sadrzi klasu Lavirint i Zid
import pygame as pg
from pygame_version import parametri


class Lavirint():
    def __init__(self, simulacija):
        self.zidovi = []
        self.zidovi.append(Zid(simulacija, 0, 0, 768, 10))
        self.zidovi.append(Zid(simulacija, 0, 758, 768, 10))
        self.zidovi.append(Zid(simulacija, 0, 0, 10, 768))
        self.zidovi.append(Zid(simulacija, 758, 0, 10, 768))
        self.zidovi.append(Zid(simulacija, 200, 0, 10, 200))
        self.zidovi.append(Zid(simulacija, 500, 200, 500, 10))
        self.zidovi.append(Zid(simulacija, 0, 350, 350, 10))
        self.zidovi.append(Zid(simulacija, 320, 450, 10, 200))
        self.zidovi.append(Zid(simulacija, 500, 200, 10, 100))
        self.zidovi.append(Zid(simulacija, 500, 600, 10, 160))


class Zid(pg.sprite.Sprite):
    def __init__(self, simulacija, x, y, width, height):
        self.grupe = simulacija.svi_sprajtovi, simulacija.lavirint_sprajtovi

        pg.sprite.Sprite.__init__(self, self.grupe)

        self.image = pg.Surface((width, height))
        self.image.fill(parametri.ZELENA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




