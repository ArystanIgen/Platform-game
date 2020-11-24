from pygame import *
import pyganim
import os
PLATFORM_WIDTH = 32
COLOR = "#888888"
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ANIMATION_DELAY= 0.1
ICON_DIR = os.path.dirname(__file__)
import pygame
dsk1=image.load('blocks/dieskelet.png')
dsk2=image.load('blocks/dieskelet2.png')
dsk1=transform.scale(dsk1,(32,32))
dsk2=transform.scale(dsk2,(32,32))
ANIMATION_DSK=[dsk1,dsk2]
ANIMATION_BLOCKTELEPORT = [
            ('%s/blocks/portal2.png' % ICON_DIR),
            ('%s/blocks/portal1.png' % ICON_DIR)]
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
class BlockTeleport(Platform):
    def __init__(self, x, y, goX, goY):
        Platform.__init__(self, x, y)
        self.goX = goX  # координаты назначения перемещения
        self.goY = goY  # координаты назначения перемещения
        boltAnim = []
        for anim in ANIMATION_BLOCKTELEPORT:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.boltAnim.blit(self.image, (0, 0))