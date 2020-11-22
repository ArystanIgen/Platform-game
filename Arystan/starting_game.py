import pygame
from pygame import *
class Game(object):
    def __init__(self):
        # Create Sprite Groups
        self.entities = pygame.sprite.Group()
        self.backentity = pygame.sprite.Group()
        self.projectilegroup = pygame.sprite.Group()
        self.enemygroup = pygame.sprite.Group()
        self.exitgroup = pygame.sprite.Group()
        self.menugroup = pygame.sprite.Group()
        self.titlegroup = pygame.sprite.Group()
        self.detectablegroup = pygame.sprite.Group()
        self.itemgroup = pygame.sprite.Group()
        self.platforms = []
        self.screenfocus = "Title"
        self.title = Title(self)
        self.pausemenu = PauseMenu(self)


class Title(object):
    def __init__(self,game):
        self.game = game
        self.counter = 0
        self.createtitle()
    def createtitle(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("title2.png")
        self.game.titlegroup.add(bg)
    def inputhandler(self):
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.game.screenfocus = "Game"
    def update(self):
        self.inputhandler()
        #Animate Title Screen
        if self.counter == 100:
            ss = Entity()
            font = pygame.font.Font(None, 60)
            ss.image = font.render("Loading...", 1,  (153, 255, 255))
            ss.rect = Rect(300,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = pygame.image.load('p_move/r1.png')
            ps.rect = Rect(265,525,200,200)
            self.game.menugroup.add(ps)
        if self.counter == 300:
            self.game.menugroup.empty()
            ss = Entity()
            font = pygame.font.Font(None, 60)
            ss.image = font.render("Featuring...", 1, (153, 255, 255))
            ss.rect = Rect(300,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = pygame.image.load("p_move/r2.png")
            ps.rect = Rect(322,525,200,200)
            self.game.menugroup.add(ps)
        if self.counter == 500:
            self.game.menugroup.empty()
            ss = Entity()
            font = pygame.font.Font(None, 60)
            ss.image = font.render("Press Start", 1,  (153, 255, 255))
            ss.rect = Rect(300,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = pygame.image.load('p_move/r_standing.png')
            ps.rect = Rect(379, 525, 200, 200)
            self.game.menugroup.add(ps)
        self.counter = self.counter + 1
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class PauseMenu(object):
    def __init__(self,game):
        self.game = game
    def createpausemenu(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("title3.jpg")
        bg.image = pygame.transform.scale(bg.image, (800, 600))
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Paused", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 290
        ss.rect.y = 400
        self.game.menugroup.add(ss)
    def inputhandler(self):
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.game.screenfocus = "Game"
    def update(self):
        self.inputhandler()