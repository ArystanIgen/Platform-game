import pygame
import os
from monsters import *
from pygame import *
from player import *
from blocks import *
from starting_game import *
import pyganim
from pygame import mixer
from pygame_menu import sound
import pygame_menu
FILE_DIR = os.path.dirname(__file__)
# Объявляем переменные
WIN_WIDTH = 800 # Ширина создаваемого окна
WIN_HEIGHT = 600  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#032973"
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)
def loadLevel(game):
    global playerX, playerY  # объявляем глобальные переменные, это координаты героя

    levelFile = open('%s/levels/1.txt' % FILE_DIR)
    line = " "
    commands = []
    while line[0] != "/":  # пока не нашли символ завершения файла
        line = levelFile.readline()  # считываем построчно
        if line[0] == "[":  # если нашли символ начала уровня
            while line[0] != "]":  # то, пока не нашли символ конца уровня
                line = levelFile.readline()  # считываем построчно уровень
                if line[0] != "]":  # и если нет символа конца уровня
                    endLine = line.find("|")  # то ищем символ конца строки
                    game.level.append(line[0: endLine])  # и добавляем в уровень строку от начала до символа "|"

        if line[0] != "":  # если строка не пустая
            commands = line.split()  # разбиваем ее на отдельные команды
            if len(commands) > 1:  # если количество команд > 1, то ищем эти команды
                if commands[0] == "player":  # если первая команда - player
                    playerX = int(commands[1])  # то записываем координаты героя
                    playerY = int(commands[2])
                if commands[0] == "monster":  # если первая команда monster, то создаем монстра
                    mn = Monster(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]),
                                 int(commands[5]), int(commands[6]))
                    game.entities.add(mn)
                    game.platforms.append(mn)
                    game.monsters.add(mn)
def main():
    pygame.font.init()
    dis=Display('')# you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Broadway', 20)
    with open("levels/names.txt", "r") as file:
        first_line = file.readline()
    name = myfont.render(first_line, False, (255, 255, 255))
    game=Game()
    pygame.init()# Инициация PyGame, обязательная строчка
    loadLevel(game)
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super p_move Boy")
    hero = Player(playerX,playerY,game)  # создаем героя по (x,y) координатам
    left = right = False
    up=down=False
    space=False
    game.entities.add(hero)
    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in game.level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                game.entities.add(pf)
                game.platforms.append(pf)
            if col == "*":
                bd = BlockDie(x, y)
                game.dieskeletgroup.add(bd)
                game.entities.add(bd)
                game.platforms.append(bd)
            if col == "C":
                cp = Cup(x, y)
                game.cupgroup.add(cp)
                game.entities.add(cp)
                game.platforms.append(cp)
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    total_level_width = len(game.level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(game.level) * PLATFORM_HEIGHT  # высоту
    camera = Camera(camera_configure, total_level_width, total_level_height)
    bg = Entity()  # Пишем в шапку
    bg.image = pygame.image.load("blocks/gif.gif")
    bg.rect = Rect(0, 0, len(game.level[0]) * PLATFORM_WIDTH, len(game.level) * PLATFORM_HEIGHT)
    bg.image = pygame.transform.scale(bg.image, (len(game.level[0]) * PLATFORM_WIDTH, len(game.level) * PLATFORM_HEIGHT))
    game.backentity.add(bg)
    mixer.music.load('AREKE.ogg')
    pygame.mixer.music.set_volume(0.05)
    mixer.music.play(-1)
    while 1:  # Основной цикл программы
        timer.tick(70)
        if game.screenfocus == "Game Over":
            for e in game.titlegroup: screen.blit(e.image, (0, 0))
            for e in game.menugroup: screen.blit(e.image, (e.rect.x, e.rect.y))
            game.gameover.update()
        if game.screenfocus == "Title":
            for e in game.titlegroup: screen.blit(e.image, (0, 0))
            for e in game.menugroup: screen.blit(e.image, (e.rect.x, e.rect.y))
            game.title.update()
        if game.screenfocus == "Pause Menu":
            for e in game.titlegroup: screen.blit(e.image, (0, 0))
            for e in game.menugroup: screen.blit(e.image, (e.rect.x, e.rect.y))
            game.pausemenu.update()
        if game.screenfocus=='Game':
            for e in pygame.event.get():  # Обрабатываем события
                if e.type == QUIT:
                    raise SystemExit
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True

                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False


                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYUP and e.key == K_UP:
                    up = False


                if e.type == KEYDOWN and e.key == K_DOWN:
                    down = True
                if e.type == KEYUP and e.key == K_DOWN:
                    down = False

                if e.type == KEYDOWN and e.key == K_SPACE:
                    space=True
                if e.type == KEYUP and e.key == K_SPACE:
                    space = False

                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    game.pausemenu.createpausemenu()
                    game.screenfocus = "Pause Menu"

            for e in game.backentity:
                screen.blit(e.image, camera.apply(e))
            #Каждую итерацию необходимо всё перерисовывать
            hero.update(left,right,up,down,space,game.platforms)
            # передвижение
            camera.update(hero)

            for e in game.monsters:
                e.update(game.platforms,game.projectilegroup)
                screen.blit(e.image, camera.apply(e))
            for e in game.dieskeletgroup:
                e.update(game.projectilegroup)
                screen.blit(e.image, camera.apply(e))
            # центризируем камеру относительно персонажа
            for e in game.entities:
                screen.blit(e.image, camera.apply(e))
            for e in game.projectilegroup:
                e.update(game.platforms)
                screen.blit(e.image,camera.apply(e))
            for e in game.cupgroup:
                screen.blit(e.image, camera.apply(e))
            screen.blit(name,(110,0))
            dis.update(hero.lifetotal[hero.currentlifetotal])
            screen.blit(dis.image,(0,0))
        if game.screenfocus == "Level Complete":
            for e in game.titlegroup: screen.blit(e.image, (0, 0))
            for e in game.menugroup: screen.blit(e.image, (e.rect.x, e.rect.y))
            game.levelcomplete.update()

        pygame.display.update()
        #обновление и вывод всех изменений на экран
if __name__ == "__main__":
    main()