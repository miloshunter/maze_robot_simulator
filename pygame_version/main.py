# Osnovni Pygame file za prikaz simulacije

import pygame as pg
import sys
import random
from pygame_version import parametri
from pygame_version.Lavirint import Lavirint
from pygame_version.Robot import Robot
import threading
from pygame_version.Partikl import Partikl
import time
from joblib import Parallel, delayed


do_parallel = False

class Simulacija:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode((parametri.SIRINA, parametri.VISINA))
        pg.display.set_caption(parametri.NASLOV)
        self.clock = pg.time.Clock()
        self.partikli = []
        self.nova_simulacija()

    def nova_simulacija(self):
        self.svi_sprajtovi = pg.sprite.Group()
        self.lavirint_sprajtovi = pg.sprite.Group()
        self.lavirint = Lavirint(self)
        self.robot = Robot(self, 150, 150)

    def glavna_petlja(self):
        # Simulira dok se self.simuliraj ne postavi na False
        self.simuliraj = True
        while self.simuliraj:
            self.dt = self.clock.tick(parametri.FPS) / 1000.0
            self.dogadjaji()
            self.crtaj()
            self.azuriraj()

    def izadji(self):
        self.tajmer_ispisa.cancel()
        pg.quit()
        sys.exit()

    def algoritam(self):

        start_time = time.time()

        partikli = simulacija.partikli

        izmerio_robot = simulacija.robot.laser.merenje_lasera

    def dogadjaji(self):
        for dogadjaj in pg.event.get():
            if dogadjaj.type == pg.QUIT:
                self.izadji()
            if dogadjaj.type == pg.KEYDOWN:
                if dogadjaj.key == pg.K_ESCAPE:
                    self.izadji()
            if dogadjaj.type == pg.KEYDOWN:
                if dogadjaj.key == pg.K_SPACE:
                    self.algoritam()
            if dogadjaj.type == pg.KEYDOWN:
                if dogadjaj.key == pg.K_p:
                    for partikl in simulacija.partikli:
                        partikl.crtaj_partikl = not partikl.crtaj_partikl

    def azuriraj(self):
        self.svi_sprajtovi.update()


    def crtaj(self):
        # Iscrtavanje sa dvostrukim baferovanjem
        self.ekran.fill(parametri.BOJA_POZADINE)


        for sprajt in self.svi_sprajtovi:
            self.ekran.blit(sprajt.image, sprajt.rect)

        pg.display.update()

simulacija = Simulacija()


def printit():
    tajmer_ispisa = threading.Timer(0.5, printit)
    simulacija.tajmer_ispisa = tajmer_ispisa
    tajmer_ispisa.setDaemon(False)
    tajmer_ispisa.start()
    print("Ispred meri       : " + str(simulacija.robot.laser_napred.merenje_lasera))
    print("Desni prednji meri: " + str(simulacija.robot.laser_desni_prednji.merenje_lasera))
    print("Desni zadnji meri : " + str(simulacija.robot.laser_desni_zadnji.merenje_lasera))


try:
  printit()
except (KeyboardInterrupt, SystemExit):
   sys.exit()


simulacija.glavna_petlja()





