import pygame
from pygame import *
from player import *
from blocks import *
from starting_game import *
import pyganim
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

def main():
    game=Game()
    xbg=ybg=0
    xbg1=-WIN_WIDTH
    ybg1=0
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super p_move Boy")
    hero = Player(55, 55,game)  # создаем героя по (x,y) координатам
    left = right = False
    up=down=False
    space=False
    game.entities.add(hero)
    level = [
        "----------------------------------",
        "-                                -",
        "-                       --       -",
        "-        *                       -",
        "-                                -",
        "-            --                  -",
        "--                               -",
        "-                                -",
        "-                   ----     --- -",
        "-                                -",
        "--                               -",
        "-            *                   -",
        "-                            --- -",
        "-                                -",
        "-                                -",
        "-  *   ---                  *    -",
        "-                                -",
        "-   -------         ----         -",
        "-                                -",
        "-                         -      -",
        "-                            --  -",
        "-           ***                  -",
        "-                                -",
        "----------------------------------"]
    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                game.entities.add(pf)
                game.platforms.append(pf)
            if col == "*":
                bd = BlockDie(x, y)
                game.entities.add(bd)
                game.platforms.append(bd)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту
    camera = Camera(camera_configure, total_level_width, total_level_height)
    bg = Entity()  # Пишем в шапку
    bg.image = pygame.image.load("blocks/gif.gif")
    bg.rect = Rect(0, 0, len(level[0]) * PLATFORM_WIDTH, len(level) * PLATFORM_HEIGHT)
    bg.image = pygame.transform.scale(bg.image, (len(level[0]) * PLATFORM_WIDTH, len(level) * PLATFORM_HEIGHT))
    game.backentity.add(bg)
    while 1:  # Основной цикл программы
        timer.tick(70)
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
            camera.update(hero)  # центризируем камеру относительно персонажа
            for e in game.entities:
                screen.blit(e.image, camera.apply(e))
            for e in game.projectilegroup:
                e.update(game.platforms)
                screen.blit(e.image,camera.apply(e))
        pygame.display.update()
        #обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()