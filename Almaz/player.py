from pygame import *

import monsters
import pyganim
import blocks
import pygame
spritesheet = pygame.image.load("blocks/bustershots2.png")
character = Surface((12,13),pygame.SRCALPHA)
character.blit(spritesheet,(-37,-80))
character = pygame.transform.scale(character, (40,20))
stage = Surface((400,250),pygame.SRCALPHA)
stage.blit(character,(40,0))
bustershot1 = stage




JUMP_POWER = 10
GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз
MOVE_SPEED = 7
WIDTH = 40
HEIGHT = 49
COLOR = "#888888"
ANIMATION_DELAY= 0.1# скорость смены кадров
ANIMATION_RIGHT = [('p_move/r1.png'),

            ('p_move/r2.png'),

            ('p_move/r3.png'),

            ('p_move/r4.png'),

            ('p_move/r5.png'),

            ('p_move/r6.png'),

            ('p_move/r7.png'),
            ('p_move/r8.png')]
ANIMATION_LEFT = [('p_move/l1.png'),

            ('p_move/l2.png'),

            ('p_move/l3.png'),

            ('p_move/l4.png'),

            ('p_move/l5.png'),

            ('p_move/l6.png'),

            ('p_move/l7.png'),


                  ('p_move/l8.png')]
ANIMATION_JUMP_LEFT = [('p_move/l_jump.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('p_move/r_jump.png', 0.1)]
ANIMATION_STAY_RIGHT = [('p_move/r_standing.png', 0.1)]
ANIMATION_STAY_LEFT = [('p_move/l_standing.png', 0.1)]
# sitting down
ANIMATION_SIT_LEFT=[('p_move/l_down.png', 0.1)]
ANIMATION_SIT_RIGHT=[('p_move/r_down.png', 0.1)]
#fire
ANIMATION_FIRE_LEFT=[('p_move/l_fire.png', 0.1)]
ANIMATION_FIRE_RIGHT=[('p_move/r_fire.png', 0.1)]

ANIMATION_OVER_LEFT=[('p_move/l_lose.png', 0.1)]
ANIMATION_OVER_RIGHT=[('p_move/r_lose.png', 0.1)]
class Player(sprite.Sprite):
    def __init__(self, x, y,game):
        sprite.Sprite.__init__(self)
        self.game=game
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.look_left=False
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        self.game_over=False
        #Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        # Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStayRight = pyganim.PygAnimation(ANIMATION_STAY_RIGHT)
        self.boltAnimStayRight.play()
        self.boltAnimStayRight.blit(self.image, (0, 0))  # По-умолчанию, стоим_вправо

        self.boltAnimStayLeft = pyganim.PygAnimation(ANIMATION_STAY_LEFT)
        self.boltAnimStayLeft.play()
        self.boltAnimStayLeft.blit(self.image, (0, 0))  # По-умолчанию, стоим_влево

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        #sitting down
        self.boltAnimSitLeft = pyganim.PygAnimation(ANIMATION_SIT_LEFT)
        self.boltAnimSitLeft.play()

        self.boltAnimSitRight = pyganim.PygAnimation(ANIMATION_SIT_RIGHT)
        self.boltAnimSitRight.play()

        #game_over
        self.boltAnimOverLeft = pyganim.PygAnimation(ANIMATION_OVER_LEFT)
        self.boltAnimOverLeft.play()

        self.boltAnimOverRight = pyganim.PygAnimation(ANIMATION_OVER_RIGHT)
        self.boltAnimOverRight.play()

        #win the game
        self.winner = False

    def update(self, left, right,up,down,space,platforms):
        if space:
            self.image.fill(Color(COLOR))
            projectile = Projectile(self,self.game)
            self.game.projectilegroup.add(projectile)


        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            if self.look_left:
                self.look_left=True# для прыжка влево есть отдельная анимация
                self.boltAnimJumpLeft.blit(self.image, (0, 0))

            else:
                self.look_left = False
                self.boltAnimJumpRight.blit(self.image, (0, 0))

        if left:
            self.look_left = True
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            if up:  # для прыжка влево есть отдельная анимация
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.look_left = False
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                if not self.look_left:
                    self.boltAnimStayRight.blit(self.image, (0, 0))
                else:
                    self.boltAnimStayLeft.blit(self.image, (0, 0))
            if down:
                self.rect.height=HEIGHT-40 # прямоугольный объект
                self.image.fill(Color(COLOR))
                if self.look_left:
                    self.look_left = True  # для прыжка влево есть отдельная анимация
                    self.boltAnimSitLeft.blit(self.image, (0, 0))
                    self.rect.height = HEIGHT

                else:
                    self.look_left = False
                    self.boltAnimSitRight.blit(self.image, (0, 0))
                    self.rect.height = HEIGHT

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel,0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if isinstance(p, blocks.BlockDie) or isinstance(p, monsters.Monster):  # если пересакаемый блок- blocks.BlockDie или Monster
                    self.die()  # умираем
                elif isinstance(p, blocks.Kubok):# если коснулись кубка
                    self.winner = True # победили!!!
                else:
                    if xvel > 0:  # если движется вправо
                        self.rect.right = p.rect.left  # то не движется вправо

                    if xvel < 0:  # если движется влево
                        self.rect.left = p.rect.right  # то не движется влево

                    if yvel > 0:  # если падает вниз
                        self.rect.bottom = p.rect.top  # то не падает вниз
                        self.onGround = True  # и становится на что-то твердое
                        self.yvel = 0  # и энергия падения пропадает

                    if yvel < 0:  # если движется вверх
                        self.rect.top = p.rect.bottom  # то не движется вверх
                        self.yvel = 0  # и энергия прыжка пропадает

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

    def die(self):
        self.image.fill(Color(COLOR))
        if not self.look_left:
            self.boltAnimOverRight.blit(self.image, (0, 0))
        else:
            self.boltAnimOverLeft.blit(self.image, (0, 0))
        time.wait(250)
        time.wait(250)
        self.teleporting(self.startX, self.startY)  # перемещаемся в начальные координаты

class Projectile(sprite.Sprite):
    def __init__(self,player,game):
        sprite.Sprite.__init__(self)
        if player.look_left==False:
            self.xvel = 15
            x = player.rect.right -60
            y = player.rect.top + 18
            self.image = bustershot1
            self.rect = Rect(x, y, 100, 20)
        else:
            self.xvel = -15
            x = player.rect.left - 340
            y = player.rect.top + 18
            self.image = pygame.transform.flip(bustershot1, True, False)
            self.rect = Rect(x, y, 500, 20)


    def update(self, platforms):
        self.rect.left += self.xvel
        self.collide(platforms)
    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.kill()
