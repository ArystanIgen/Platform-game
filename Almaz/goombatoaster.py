spritesheet = pygame.image.load("smbenemiessheet.png")

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(0,-4))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
goombaleft = stage

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-30,-4))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
goombaright = stage

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-60,0))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,150),pygame.SRCALPHA)
stage.blit(character,(130,30))
goombadead = stage

goombawalk = [goombaleft, goombaright]

#Load Explosion Sprite Sheet

spritesheet = pygame.image.load("explosion.png")

explodex = 68
explodey = -6

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-117))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode1 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-181))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode2 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-245))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode3 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-309))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode4 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-373))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode5 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-437))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode6 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-502))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode7 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-566))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode8 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-631))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode9 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-696))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode10 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-760))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode11 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-761))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode11 = stage

character = Surface((97,50),pygame.SRCALPHA)
character.blit(spritesheet,(-228,-826))
character = pygame.transform.scale(character, (97*2,50*2))
stage = Surface((300,450),pygame.SRCALPHA)
stage.blit(character,(explodex,explodey))
explode12 = stage

explosion = [explode1,explode2,explode3,explode4,explode5,explode6,explode7,explode8,explode9,explode10,explode11,explode12]

#Load Bubble Bobble Enemies Sprite Sheet

spritesheet = pygame.image.load("bubblebobble.png")

character = Surface((14,16),pygame.SRCALPHA)
character.blit(spritesheet,(-6,-5))
character = pygame.transform.scale(character, (14*4,16*4))
stage = Surface((300,16*4),pygame.SRCALPHA)
stage.blit(character,(130,0))
toasterwalk1 = stage

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-26,-5))
character = pygame.transform.scale(character, (16*4,16*4))
stage = Surface((300,16*4),pygame.SRCALPHA)
stage.blit(character,(130,0))
toasterwalk2 = stage

toasterwalkloop = [toasterwalk1,toasterwalk2]
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
class Goomba(Entity):
    def __init__(self, x, y, xvel):
        Entity.__init__(self)
        #Set Velocities
        self.xvel = xvel
        self.yvel = 0
        #States
        self.onGround = False
        self.airborne = True
        self.destroyed = False
        #Offsets
        self.xoffset = -130
        self.yoffset = -30
        #Counter
        self.counter = 0
        #Create Sprite Image
        self.image = Surface((300, 450), pygame.SRCALPHA)
        self.image = goombaleft
        self.rect = Rect(x, y, 300, 450)
        #Create Detectable


    def update(self, platforms, projectilegroup):
        #Move
        if self.yvel < 0: self.airborne = True
        if self.onGround == True: self.airborne = False
        if not self.onGround:
            self.yvel += 0.3
            if self.yvel > 1.2: self.airborne = True
            if self.yvel > 100: self.yvel = 100

        #Collisions
        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms, projectilegroup)
        self.rect.top += self.yvel
        self.onGround = False;
        self.collide(0, self.yvel, platforms, projectilegroup)

        #Apply Offsets
        self.rect.x = self.rect.x + self.xoffset
        self.rect.y = self.rect.y + self.yoffset

        #Animate
        self.animate()
    
    def collide(self, xvel, yvel, platforms, projectilegroup):
        #Collide Platforms
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -2
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = 2
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        #Collide Projectiles
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self, j):
                self.xvel = 0
                self.destroyed = True

    #Animate
    def animate(self):
        if self.destroyed == True:
            self.destroyloop(explosion)
        else:
            self.walkloop(goombawalk)
    #Walk Loop Animation
    def walkloop(self, loop):
        if self.counter == 10: self.updatecharacter(loop[0])
        elif self.counter == 20:
            self.updatecharacter(loop[1])
            self.counter = 0
        self.counter = self.counter + 1
    #Destroy Loop Animation
    def destroyloop(self,loop):
        if self.counter == 0: self.updatecharacter(loop[0])
        elif self.counter == 5: self.updatecharacter(loop[1])
        elif self.counter == 10: self.updatecharacter(loop[2])
        elif self.counter == 15: self.updatecharacter(loop[3])
        elif self.counter == 20: self.updatecharacter(loop[4])
        elif self.counter == 25: self.updatecharacter(loop[5])
        elif self.counter == 30: self.updatecharacter(loop[6])
        elif self.counter == 35: self.updatecharacter(loop[7])
        elif self.counter == 40: self.updatecharacter(loop[8])
        elif self.counter == 45: self.updatecharacter(loop[9])
        elif self.counter == 50: self.updatecharacter(loop[10])
        elif self.counter == 55: self.updatecharacter(loop[11])
        elif self.counter == 60:
            self.kill()
            self.counter = 0
        self.counter = self.counter + 1
    #Update Animation Frame
    def updatecharacter(self, ansurf): self.image = ansurf
        
class Toaster(Entity):
    def __init__(self, x, y, track, xvel):
        Entity.__init__(self)
        #Set Velocities
        self.xvel = xvel
        self.yvel = 0
        #States
        self.destroyed = False
        self.faceright = False
        self.onGround = False
        self.airborne = True
        #Offests
        self.xoffset = -130
        self.yoffset = 0
        #Counter
        self.counter = 0
        #Configure Track
        if xvel > 0:
            self.min = x
            self.max = x + track
        elif xvel < 0:
            self.max = x
            self.min = x - track
        #Create Sprite Image
        self.image = Surface((300, 450), pygame.SRCALPHA)
        self.image = toasterwalk1
        self.rect = Rect(x, y, 300, 450)
        #Create Dectectable
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(x, y, 64,64)
        self.detectable.image = Surface((64,64))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()

    def update(self, platforms, projectilegroup):
        #Move
        if self.xvel > 0: self.faceright = True
        if self.xvel < 0: self.faceright = False
        self.detectable.rect.left += self.xvel
        if self.detectable.rect.left == self.max: self.xvel = -abs(self.xvel)
        if self.detectable.rect.left == self.min: self.xvel = abs(self.xvel)
        self.detectable.rect.top += self.yvel

        #Collisions
        self.collide(0, self.yvel, platforms, projectilegroup)
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        #Animate
        self.animate()
    
    def collide(self, xvel, yvel, platforms, projectilegroup):
        #Collide Projectiles
        for j in projectilegroup:
            if pygame.sprite.collide_rect(self.detectable, j):
                self.destroyed = True
                self.counter = 0
                self.xvel = 0

    #Animate          
    def animate(self):
        if self.destroyed == True:
            self.destroyloop(explosion)
        else:
            self.walkloop(toasterwalkloop)
    #Walk Loop Animation
    def walkloop(self, loop):
        if self.counter == 10:
            self.updatecharacter(loop[0])
            if self.faceright == True: self.updatecharacter(pygame.transform.flip(loop[0], True, False))
        elif self.counter == 20:
            self.updatecharacter(loop[1])
            if self.faceright == True: self.updatecharacter(pygame.transform.flip(loop[1], True, False))
            self.counter = 0
        self.counter = self.counter + 1
    #Destroy Loop Animation
    def destroyloop(self,loop):
        if self.counter == 0:
            self.yoffset = -30
            self.updatecharacter(loop[0])
        elif self.counter == 5: self.updatecharacter(loop[1])
        elif self.counter == 10: self.updatecharacter(loop[2])
        elif self.counter == 15: self.updatecharacter(loop[3])
        elif self.counter == 20: self.updatecharacter(loop[4])
        elif self.counter == 25: self.updatecharacter(loop[5])
        elif self.counter == 30: self.updatecharacter(loop[6])
        elif self.counter == 35: self.updatecharacter(loop[7])
        elif self.counter == 40: self.updatecharacter(loop[8])
        elif self.counter == 45: self.updatecharacter(loop[9])
        elif self.counter == 50: self.updatecharacter(loop[10])
        elif self.counter == 55: self.updatecharacter(loop[11])
        elif self.counter == 60:
            self.kill()
            self.counter = 0
        self.counter = self.counter + 1
    #Update Animation Frame
    def updatecharacter(self, ansurf): self.image = ansurf
