import os
import pygame
from pygame_menu import sound
import pygame_menu

FPS = 30.0
H_SIZE = 600
W_SIZE = 800


pygame.init()
HELP = "TROIA"
INFO = "О нас: Igen Arystan, "\
       "Tokumtayev Rakhat, "\
       "Iztay Almaz "
COLOR = "СИНИЙ " \
        ""\
         " ЗЕЛЕНЫЙ" \
        ""\
         " СЕРЫЙ" \
        ""\
         " КРАСНЫЙ" \
        ""\


surface = pygame.display.set_mode((700, 500))



def func(name):
    print("Hello world from", name)  # name will be 'foo'


menu = pygame_menu.Menu(400, 500, 'Игра', theme=pygame_menu.themes.THEME_SOLARIZED,)
menu.add_text_input('Имя :', default='Player', background_color=(0,0,0))
menu.add_button(' Выход ', pygame_menu.events.EXIT, background_color=(0,0,0))


about_menu = pygame_menu.Menu(400, 500, "О нас",theme=pygame_menu.themes.THEME_SOLARIZED)
PATH = os.path.join(os.path.dirname(pygame_menu.__file__),
                    'resources', 'images', 'pygame_menu.png')
menu.add_button(about_menu.get_title(), about_menu,shadow=True, shadow_color=(0, 0, 100),background_color=(0,0,0))
about_menu.add_image(PATH, angle=-10, scale=(0.15, 0.15), scale_smooth=True)
about_menu.add_label('Tokumtayev Rakhat')
about_menu.add_vertical_margin(50)
about_menu.add_image(PATH, angle=10, scale=(0.15, 0.15))
about_menu.add_label('Iztay Almaz')
about_menu.add_vertical_margin(50)
about_menu.add_image(PATH, angle=-10, scale=(0.15, 0.15), scale_smooth=True)
about_menu.add_label('Igen Arystan')


#color_menu = pygame_menu.Menu(400, 500, "Персонаж",theme=pygame_menu.themes.THEME_SOLARIZED)
#menu.add_button(color_menu.get_title(), color_menu,shadow=True, shadow_color=(0, 0, 100),background_color=(0,0,0))

#color_menu.add_button(' Красный ', pygame_menu.events.BACK,shadow=True , background_color=(0,0,0))
#color_menu.add_button(' Серый ', pygame_menu.events.BACK,shadow=True, background_color=(0,0,0))
#color_menu.add_button(' Зеленый ', pygame_menu.events.BACK,shadow=True, background_color=(0,0,0))
#color_menu.add_button(' Синий ', pygame_menu.events.BACK,shadow=True, background_color=(0,0,0))

menu.add_label(HELP, max_char=-1, font_size=20, margin=(0,0))
menu.mainloop(surface)



