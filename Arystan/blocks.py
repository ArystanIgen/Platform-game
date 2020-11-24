from pygame import *
import pyganim
PLATFORM_WIDTH = 32
COLOR = "#888888"
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ANIMATION_DELAY= 0.1
import pygame
dsk1=image.load('blocks/dieskelet.png')
dsk2=image.load('blocks/dieskelet2.png')
dsk1=transform.scale(dsk1,(32,32))
dsk2=transform.scale(dsk2,(32,32))
ANIMATION_DSK=[dsk1,dsk2]
class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((32,32))
        self.image = image.load("blocks/platform.png")
        self.rect = Rect(x, y,40,40)
        boltAnim = []
        for anim in ANIMATION_DSK:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimDsk = pyganim.PygAnimation(boltAnim)
        self.boltAnimDsk.play()
class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(COLOR))
        self.image.set_colorkey(Color(COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH-5, PLATFORM_HEIGHT-5)
    def update(self,projectilegroup):
        self.image.fill(Color(COLOR))
        self.boltAnimDsk.blit(self.image, (0, 0))
        self.collide(projectilegroup)
    def collide(self,projectilegroup):
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self,j):
                self.kill()
class Cup(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("blocks/cup.png")