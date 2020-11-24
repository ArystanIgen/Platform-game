import pygame
import os
import tmxreader # Может загружать tmx файлы
import helperspygame # Преобразует tmx карты в формат  спрайтов pygame
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
CENTER_OF_SCREEN = WIN_WIDTH / 2, WIN_HEIGHT / 2

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    def reverse(self, pos):  # получение внутренних координат из глобальных
        return pos[0] - self.state.left, pos[1] - self.state.top


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)
def loadLevel(name,game):
    global playerX, playerY # объявляем глобальные переменные, это координаты героя
    global total_level_height, total_level_width
    global sprite_layers # все слои карты
    world_map = tmxreader.TileMapParser().parse_decode('%s/%s.tmx' % (FILE_DIR, name)) # загружаем карту
    resources = helperspygame.ResourceLoaderPygame() # инициируем преобразователь карты
    resources.load(world_map) # и преобразуем карту в понятный pygame формат

    sprite_layers = helperspygame.get_layers_from_map(resources) # получаем все слои карты

    # берем слои по порядку 0 - слой фона, 1- слой блоков, 2 - слой смертельных блоков
    # 3 - слой объектов монстров, 4 - слой объектов телепортов
    platforms_layer = sprite_layers[1]
    dieBlocks_layer = sprite_layers[2]

    for row in range(0, platforms_layer.num_tiles_x): # перебираем все координаты тайлов
        for col in range(0, platforms_layer.num_tiles_y):
            if platforms_layer.content2D[col][row] is not None:
                pf = Platform(row * PLATFORM_WIDTH, col * PLATFORM_WIDTH)# как и прежде создаем объкты класса Platform
                game.entities.add(pf)
                game.platforms.append(pf)

            if dieBlocks_layer.content2D[col][row] is not None:
                bd = BlockDie(row * PLATFORM_WIDTH, col * PLATFORM_WIDTH)
                game.dieskeletgroup.add(bd)
                game.entities.add(bd)
                game.platforms.append(bd)

    teleports_layer = sprite_layers[4]
    for teleport in teleports_layer.objects:
        try: # если произойдет ошибка на слое телепортов
            goX = int(teleport.properties["goX"]) * PLATFORM_WIDTH+35
            goY = int (teleport.properties["goY"]) * PLATFORM_HEIGHT
            x = teleport.x
            y = teleport.y - PLATFORM_HEIGHT
            tp = BlockTeleport(x, y, goX, goY)
            game.entities.add(tp)
            game.platforms.append(tp)
            game.teleport.add(tp)
        except: # то игра не вылетает, а просто выводит сообщение о неудаче
            print(u"Ошибка на слое телепортов")

    monsters_layer = sprite_layers[3]
    for monster in monsters_layer.objects:
        try:
            x = monster.x
            y = monster.y
            if monster.name == "Player":
                playerX = x
                playerY = y - PLATFORM_HEIGHT
            elif monster.name == "Princess":
                cp = Cup(x, y-10)
                game.cupgroup.add(cp)
                game.entities.add(cp)
                game.platforms.append(cp)

            else:
                up = int(monster.properties["up"])
                maxUp = int(monster.properties["maxUp"])
                left = int(monster.properties["left"])
                maxLeft = int(monster.properties["maxLeft"])
                mn = Monster(x, y - PLATFORM_HEIGHT, left, up, maxLeft, maxUp)
                game.monsters.add(mn)
        except:
            print(u"Ошибка на слое монстров")

    total_level_width = platforms_layer.num_tiles_x * PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
    total_level_height = platforms_layer.num_tiles_y * PLATFORM_HEIGHT   # высоту
def main():
    pygame.font.init()
    dis=Display()# you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Broadway', 20)
    with open("levels/names.txt", "r") as file:
        first_line = file.readline()
    name = myfont.render(first_line, False, (255, 255, 255))
    game=Game()
    pygame.init()# Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем око
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))# шко
    pygame.display.set_caption("Super p_move Boy")
    renderer = helperspygame.RendererPygame()
    for lvl in range(1, 4):
        loadLevel("levels/map_1",game)
        bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
        left = right = False
        up = down = False
        space = False
        try:
            hero = Player(playerX, playerY,game)  # создаем героя по (x,y) координатам
            game.entities.add(hero)
        except:
            print(u"Не удалось на карте найти героя, взяты координаты по-умолчанию")
            hero = Player(65, 65,game)
        game.entities.add(hero)
        timer = pygame.time.Clock()
        camera = Camera(camera_configure, total_level_width, total_level_height)
        bg = Entity()  # Пишем в шапку
        bg.image = pygame.image.load("blocks/gif.gif")
        bg.rect = Rect(0, 0, total_level_width, total_level_height)
        bg.image = pygame.transform.scale(bg.image, (total_level_width, total_level_height))
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
                for sprite_layer in sprite_layers:  # перебираем все слои
                    if not sprite_layer.is_object_group:  # и если это не слой объектов
                        renderer.render_layer(screen, sprite_layer)  # отображаем его

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
                for e in game.teleport:
                    e.update()
                    screen.blit(e.image,camera.apply(e))
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

            pygame.display.update()# ж
        #обновление и вывод всех изменений на экран
if __name__ == "__main__":
    main()