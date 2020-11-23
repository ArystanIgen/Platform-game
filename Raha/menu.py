#WHITE  = (255, 255, 255)
#BLACK  = (0, 0, 0)
#RED    = (255, 0, 0)
#GREEN  = (0, 255, 0)
#BLUE   = (0, 0, 255)
#YELLOW = (255, 255, 0)


import os
import pygame
from pygame_menu import sound
import pygame_menu

engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'Mouse Click Fast.wav')

FPS = 30.0
H_SIZE = 600
W_SIZE = 800


pygame.init()
HELP = " TROIA  TEAM"

surface = pygame.display.set_mode((700, 500))


menu = pygame_menu.Menu(400, 500, 'STORM GLASS', theme=pygame_menu.themes.THEME_BLUE,)
menu.set_sound(engine, recursive=True) #добавляем звук клика мыши в основное меню
menu.add_text_input('Имя :',shadow=True ,shadow_color=(0, 0, 100), default='Игрок', background_color=(255,255,255))
menu.add_button(' Выход ', pygame_menu.events.EXIT,shadow=True ,shadow_color=(0, 0, 100), background_color=(255,255,255))


about_menu = pygame_menu.Menu(400, 500, "О нас",theme=pygame_menu.themes.THEME_BLUE)
PATH = os.path.join(os.path.dirname(pygame_menu.__file__),
                    'resources', 'images', 'pygame_menu.png')
menu.add_button(about_menu.get_title(), about_menu,shadow=True, shadow_color=(0, 0, 100),background_color=(255,255,255))
about_menu.add_image(PATH, angle=-10, scale=(0.15, 0.15), scale_smooth=True)
about_menu.add_label('Tokumtayev Rakhat')
about_menu.add_vertical_margin(50)
about_menu.add_image(PATH, angle=10, scale=(0.15, 0.15))
about_menu.add_label('Iztay Almaz')
about_menu.add_vertical_margin(50)
about_menu.add_image(PATH, angle=-10, scale=(0.15, 0.15), scale_smooth=True)
about_menu.add_label('Igen Arystan')
about_menu.add_vertical_margin(50)
about_menu.add_image(PATH, angle=10, scale=(0.15, 0.15), scale_smooth=True)
about_menu.add_label('Zhenis Nursultan')



color_menu = pygame_menu.Menu(400, 500, "Персонаж" ,theme=pygame_menu.themes.THEME_BLUE)
menu.add_button(color_menu.get_title(), color_menu,shadow=True, shadow_color=(0, 0, 100),background_color=(255,255,255))
color_menu.set_sound(engine, recursive=True)
color_menu.add_button(' Красный ', pygame_menu.events.BACK,shadow=True ,shadow_color=(0, 0, 100),background_color=(255,255,255))
color_menu.add_button(' Серый ', pygame_menu.events.BACK,shadow=True,shadow_color=(0, 0, 100), background_color=(255,255,255))
color_menu.add_button(' Зеленый ', pygame_menu.events.BACK,shadow=True,shadow_color=(0, 0, 100), background_color=(255,255,255))
color_menu.add_button(' Синий ', pygame_menu.events.BACK,shadow=True,shadow_color=(0, 0, 100), background_color=(255,255,255)t)

menu.add_label(HELP, max_char=-1, font_size=20, margin=(0,0))
menu.mainloop(surface)

