import pygame
# вначале Ареке создаем список
win = pygame.display.set_mode(500,500)
bullets = []
lastMove = "right" # это для facing, чтобы знать куда он стрелял влево или вправо
#дальше в основном цикле будем писать где у тебя while
run = True
class strelyat():
    def _init_(self, x,y,radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8*facing #facing это куда пуля полетить
    def draw(self, win):# win это то окно, где мы будем рисовать снаряды короче
            pygame.draw.rect(win, self.color, (self.x, self.y), self.radius)

def drawWindow():# это метод где ты будешь рисовать пули  своего игрока и так далее...
    for bullet in bullets:
        bullet.draw(win)

while run:
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0: #500 и 0 короче это размер нашего окна, пока наша пуля не вышла из окна делаем что-то
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1# справо
        else:
            facing = -1# слево
#Еще Ареке lastMove добавь в движения игрока, потому что а то не будет работать
#Типа:
    """if keys[pygame.K_LEFT] and x > 5:
    ...
    lastMove = 'left'
    """
    if len(bullets) < 11: # это короче количество пуль, когда за рамки окна уйдут они удалятся и марио может обратно столько стрелять
        bullets.append(strelyat(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))#width and height размер игрока