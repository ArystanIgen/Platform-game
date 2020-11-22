from pygame import *
import pyganim
import blocks
import player
velocity = 6
WIDTH = 40
HEIGHT = 49
COLOR = "#888888"
class enemy(object):
    def __init__(self, x, y, width, height,color,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.draw.rect(win,self.color, (self.x,self.y), )
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    pygame.display.update()

#все что ниже в main надо засунуть, а всё что сверху надо в ботс добавить
#mainloop
bot = enemy(100, 410, 64, 64, 300)
bullets = []
run = True
while run:
    redrawGameWindow()
pygame.quit()
