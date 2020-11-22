spritesheet = pygame.image.load("Media/Graphics/item.png")

character = Surface((78, 59), pygame.SRCALPHA)
character.blit(spritesheet, (-37, -4))
character = pygame.transform.scale(character, (78 * 3, 59 * 3))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
itemframe1 = stage #pervaya stadia svecheniya priza

character = Surface((78, 59), pygame.SRCALPHA)
character.blit(spritesheet, (-37, -66))
character = pygame.transform.scale(character, (78 * 3, 59 * 3))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
itemframe2 = stage  #vtoraya stadia svecheniya priza

character = Surface((78, 59), pygame.SRCALPHA)
character.blit(spritesheet, (-37, -128))
character = pygame.transform.scale(character, (78 * 3, 59 * 3))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
itemframe3 = stage #tret'ya stadia svecheniya priza

itemloop = [itemframe1, itemframe2, itemframe3]

class Item(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = itemframe1 #картинка кубка
        self.rect = Rect(x*3,y*3,78*3,59*3)
        self.counter = 0
        self.detectable = pygame.sprite.Sprite() #sozdaet object
        self.detectable.rect = Rect(x*3, y*3, 64,64)
        self.detectable.rect.x = self.detectable.rect.x + 190
        self.detectable.rect.y = self.detectable.rect.y + 60
        self.detectable.image = Surface((64,64))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()
    def update(self):
        if self.counter == 0: self.image = itemloop[0] #если количество кадров в секунду =0 => показываем первую
                                                        #стадию свечения кубка
        if self.counter == 10: self.image = itemloop[1] #если количество кадров в секунду =10 => показываем вторую
                                                        #стадию свечения кубка

        if self.counter == 20: #если количество кадров в секунду =20 => показываем последнюю стадию
                                                        # свечения кубка, затем обнуляем counter

            self.image = itemloop[2]
            self.counter = 0
        self.counter = self.counter + 1

class PauseMenu(object):
    def __init__(self,game):
        self.game = game
    def createpausemenu(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Пауза", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 290
        ss.rect.y = 400
        self.game.menugroup.add(ss)
    def inputhandler(self):
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_RETURN:
                self.game.screenfocus = "Game"
    def update(self):
        self.inputhandler()

class LevelComplete(object):
    def __init__(self,game):
        self.game = game
    def createlevelcomplete(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Level Complete", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 200
        ss.rect.y = 400
        self.game.menugroup.add(ss)
        
class GameOver(object):
    def __init__(self,game):
        self.game = game
    def creategameover(self):
        #Empty Sprite Groups
        self.game.titlegroup.empty()
        self.game.menugroup.empty()
        #Create Background Sprite
        bg = Entity()
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
        self.game.titlegroup.add(bg)
        #Create String Sprite
        ss = Entity()
        font = pygame.font.Font(None, 80)
        ss.image = font.render("Game Over", 1, (255, 255, 255))
        ss.rect = Rect(0,0,100,100)
        ss.rect.x = 240
        ss.rect.y = 400
        self.game.menugroup.add(ss)
    
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
        bg.image = pygame.image.load("Media/Graphics/Backgrounds/title.jpg")
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
            font = pygame.font.Font(None, 80)
            ss.image = font.render("Starring", 1, (255, 255, 255))
            ss.rect = Rect(280,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = standleft
            ps.rect = Rect(230,500,200,200)
            self.game.menugroup.add(ps)
        if self.counter == 300:
            self.game.menugroup.empty()
            ss = Entity()
            font = pygame.font.Font(None, 80)
            ss.image = font.render("Featuring", 1, (255, 255, 255))
            ss.rect = Rect(260,400,100,100)
            self.game.menugroup.add(ss)
            ps = Entity()
            ps.image = goombaleft
            ps.rect = Rect(230,500,200,200)
            self.game.menugroup.add(ps)
        if self.counter == 500:
            self.game.menugroup.empty()
            ss = Entity()
            font = pygame.font.Font(None, 80)
            ss.image = font.render("Press Start", 1, (255, 255, 255))
            ss.rect = Rect(240,400,100,100)
            self.game.menugroup.add(ss)
        self.counter = self.counter + 1


class Game(object):
    def __init__(self):
        # Create Sprite Groups
        self.entities = pygame.sprite.Group()
        self.playerentity = pygame.sprite.Group()
        self.projectilegroup = pygame.sprite.Group()
        self.enemygroup = pygame.sprite.Group()
        self.exitgroup = pygame.sprite.Group()
        self.menugroup = pygame.sprite.Group()
        self.titlegroup = pygame.sprite.Group()
        self.detectablegroup = pygame.sprite.Group()
        self.itemgroup = pygame.sprite.Group()
        # Create Camera
        self.camera = ""
        self.camerafocus = ""
        # Create Platforms
        self.platforms = []
        # Create Screen Focus
        self.screenfocus = "Title"
        # Create Title
        self.title = Title(self)
        # Create Gameover
        self.gameover = GameOver(self)
        # Create Level Complete
        self.levelcomplete = LevelComplete(self)
        # Create Pause Menu
        self.pausemenu = PauseMenu(self)


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)