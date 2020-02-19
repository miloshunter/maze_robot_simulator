# Klasa za robota koji ce ici po lavirintu i meriti
import pygame as pg
from pygame_version.Laser import Laser
vec = pg.math.Vector2



class Robot(pg.sprite.Sprite):
    def __init__(self, simulacija, x, y):
        self.grupe = simulacija.svi_sprajtovi
        self.simulacija = simulacija

        pg.sprite.Sprite.__init__(self, self.grupe)

        self.original_image = pg.image.load("robot.png")
        self.original_image = pg.transform.scale(self.original_image, (40, 40))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rot_speed = 3
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 45

        self.laser = Laser(self)

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = 5
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -5
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(2, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-2 / 2, 0).rotate(-self.rot)

        new_sprite = pg.sprite.Sprite()
        new_rect = pg.Rect(self.rect)
        new_rect.x += self.vel[0]
        new_rect.y += self.vel[1]
        new_sprite.rect = new_rect
        if pg.sprite.spritecollide(new_sprite, self.simulacija.lavirint_sprajtovi, False):
            self.vel = vec(0, 0)

    def update(self):
        self.get_keys()
        self.rot += self.rot_speed
        self.pos += self.vel
        self.image = pg.transform.rotate(self.original_image, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
