from pygame import *
import pyganim
import blocks
import pygame
from starting_game import *
import monsters
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
#falling
ANIMATION_FALLING_LEFT=[('p_move/l_jump.png', 0.1)]
ANIMATION_FALLING_RIGHT=[('p_move/r_jump.png', 0.1)]

#jump fire
ANIMATION_FIREJ_LEFT=[('p_move/l_j_f.png', 0.1)]
ANIMATION_FIREJ_RIGHT=[('p_move/r_j_f.png', 0.1)]

#BULLETS--------------------------------
ANIMATION_BULLET_LEFT=[
    ('bullets/fl1.png'),
]
ANIMATION_BULLET_RIGHT=[
    ('bullets/fr1.png')
]

h1=pygame.image.load('blocks/1h.png')
h2=pygame.image.load('blocks/2h.png')
h3=pygame.image.load('blocks/3h.png')
h4=pygame.image.load('blocks/4h.png')
h5=pygame.image.load('blocks/5h.png')

class Player(sprite.Sprite):
    def __init__(self, x, y,game):
        sprite.Sprite.__init__(self)
        self.game=game
        self.damage=False
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.collideright = False
        self.takingdamage = False
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.look_left=False
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        self.game_over=False
        self.lifetotal = [h1,h1,h2,h3,h4,h5]
        self.currentlifetotal = 5
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
        #falling
        self.boltAnimFallingLeft = pyganim.PygAnimation(ANIMATION_FALLING_LEFT)
        self.boltAnimFallingLeft.play()

        self.boltAnimFallingRight = pyganim.PygAnimation(ANIMATION_FALLING_RIGHT)
        self.boltAnimFallingRight.play()
        #game_over
        self.boltAnimOverLeft = pyganim.PygAnimation(ANIMATION_OVER_LEFT)
        self.boltAnimOverLeft.play()

        self.boltAnimOverRight = pyganim.PygAnimation(ANIMATION_OVER_RIGHT)
        self.boltAnimOverRight.play()
        #fire
        self.boltAnimFireLeft = pyganim.PygAnimation(ANIMATION_FIRE_LEFT)
        self.boltAnimFireLeft.play()

        self.boltAnimFireRight = pyganim.PygAnimation(ANIMATION_FIRE_RIGHT)
        self.boltAnimFireRight.play()

        self.boltAnimFireJLeft = pyganim.PygAnimation(ANIMATION_FIREJ_LEFT)
        self.boltAnimFireJLeft.play()

        self.boltAnimFireJRight = pyganim.PygAnimation(ANIMATION_FIREJ_RIGHT)
        self.boltAnimFireJRight.play()


    def update(self, left, right,up,down,space,platforms):

        if space:
            projectile = Projectile(self,self.game)
            self.game.projectilegroup.add(projectile)

        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER

            self.image.fill(Color(COLOR))
            if space:
                self.image.fill(Color(COLOR))
                projectile = Projectile(self, self.game)
                self.game.projectilegroup.add(projectile)

                if not self.look_left:
                    self.boltAnimFireJRight.blit(self.image, (0, 0))
                else:
                    self.boltAnimFireJLeft.blit(self.image, (0, 0))
            else:
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
                if space:
                    projectile = Projectile(self, self.game)
                    self.game.projectilegroup.add(projectile)
                    self.boltAnimFireJLeft.blit(self.image, (0, 0))

                else:
                    self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.look_left = False
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            if up:
                if space:
                    projectile = Projectile(self, self.game)
                    self.game.projectilegroup.add(projectile)
                    self.boltAnimFireJRight.blit(self.image, (0, 0))
                else:
                    self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                if space:
                    self.image.fill(Color(COLOR))
                    projectile = Projectile(self, self.game)
                    self.game.projectilegroup.add(projectile)
                    if not self.look_left:
                        self.boltAnimFireRight.blit(self.image, (0, 0))
                    else:
                        self.boltAnimFireLeft.blit(self.image, (0, 0))
                else:
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
        if self.yvel>1:
            if not space:
                self.image.fill(Color(COLOR))
                if self.look_left:
                    self.look_left = True  # для прыжка влево есть отдельная анимация
                    self.boltAnimFallingLeft.blit(self.image, (0, 0))


                else:
                    self.look_left = False
                    self.boltAnimFallingRight.blit(self.image, (0, 0))
        if not self.onGround:
            '''
            self.image.fill(Color(COLOR))
            if self.look_left:
                self.look_left = True  # для прыжка влево есть отдельная анимация
                self.boltAnimFallingLeft.blit(self.image, (0, 0))
                

            else:
                self.look_left = False
                self.boltAnimFallingRight.blit(self.image, (0, 0))
            '''
            self.yvel += GRAVITY
        if self.takingdamage:
            if self.collideright:
                self.xvel = -8
            else:
                self.xvel = 8
        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms,self.game)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel,0, platforms,self.game)

    def collide(self, xvel, yvel, platforms,game):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if isinstance(p, blocks.BlockDie) or isinstance(p,monsters.Monster):  # если пересакаемый блок- blocks.BlockDie или Monster
                    self.die()
                    self.currentlifetotal = self.currentlifetotal - 1
                    if self.currentlifetotal <= 0:
                        game.gameover.creategameover()
                        game.screenfocus = "Game Over"
                        self.currentlifetotal = 0
                elif isinstance(p, blocks.Cup):  # если коснулись принцессы
                    self.game.levelcomplete.createlevelcomplete()
                    self.game.screenfocus = "Level Complete"
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
        for j in self.game.dieskeletgroup:
            if sprite.collide_rect(self, j):
                leftdifference = self.rect.right
                rightdifference = self.rect.left
                if self.xvel == 0:
                    if abs(leftdifference) < 10: self.collideright = True
                    if abs(rightdifference) < 10: self.collideright = False
                self.takingdamage = True
                self.currentlifetotal = self.currentlifetotal - 1
                if self.currentlifetotal <= 0:
                    game.gameover.creategameover()
                    game.screenfocus = "Game Over"
                    self.currentlifetotal = 0


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
        self.image = Surface((20,10))
        self.image.set_colorkey(Color(COLOR))
        self.looking_left=False
        boltAnim = []
        for anim in ANIMATION_BULLET_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimBulletRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimBulletRight.play()
        # Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_BULLET_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimBulletLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimBulletLeft.play()
        if player.look_left==False:
            self.looking_left=False
            self.xvel = 15
            self.image=pygame.image.load("bullets/fr11.png")
            x = player.rect.right -25
            y = player.rect.top + 10
            self.rect = Rect(x, y, 20, 20)
        else:
            self.looking_left=True
            self.xvel = -15
            self.image = pygame.image.load("bullets/fl11.png")
            x = player.rect.left-7
            y = player.rect.top + 10
            self.rect = Rect(x, y,20 , 20)

    def update(self, platforms):
        self.rect.left += self.xvel
        self.collide(platforms)
    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.kill()

