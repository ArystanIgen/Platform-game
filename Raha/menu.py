#WHITE  = (255, 255, 255)
#BLACK  = (0, 0, 0)
#RED    = (255, 0, 0)
#GREEN  = (0, 255, 0)
#BLUE   = (0, 0, 255)
#YELLOW = (255, 255, 0)


import os,sys
import pygame
from pygame_menu import sound
import pygame_menu
from pygame import mixer


def data_fun():
    filename = 'levels/names.txt'
    data = menu.get_input_data()
    for k in data.keys():
        l=data[k]
    with open(filename, 'w') as file_object:
        file_object.write(l)
pygame.init()  # инициализировал миксер
mixer.music.load('jr.mp3')
mixer.music.play(0, 20)  # loop
pygame.mixer.music.set_volume(0.06)

engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'Mouse Click Fast.wav')

FPS = 30.0
H_SIZE = 600
W_SIZE = 800
pygame.init()
HELP = " TROIA  TEAM"

font = pygame_menu.font.FONT_8BIT
mytheme = pygame_menu.themes.Theme(widget_font=font,background_color=(0, 0, 0, 0),  # transparent background
                title_shadow=True,
                title_background_color=(4, 47, 126))
myimage = pygame_menu.baseimage.BaseImage(
    image_path='space.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
mytheme.background_color = myimage
surface = pygame.display.set_mode((800, 600))
bg=pygame.image.load("space.png")
menu = pygame_menu.Menu(600, 800, 'STORM GLASS', theme=mytheme)
menu.set_sound(engine, recursive=True)  # добавляем звук клика мыши в основное меню
menu.add_text_input('NAME ', font_color=(0,252,255),shadow_color=(255,0,0),shadow=True, default='PLAYER',background_color=(0, 0, 0,0))
menu.add_button('SAVE NAME', data_fun,font_size=40,font_color=(255,0,0),shadow_color=(0,0,0,0),shadow=True,background_color=(0,0,0,0))

about_menu = pygame_menu.Menu(600, 800, "ABOUT", theme=mytheme)
PATH = os.path.join(os.path.dirname(pygame_menu.__file__),
                    'resources', 'images', 'pygame_menu.png')
menu.add_button(about_menu.get_title(), about_menu, font_color=(0,252,255),shadow_color=(255,0,0),shadow=True,background_color=(0,0,0,0))
about_menu.add_label('Tokumtayev Rakhat',font_color=(0,252,255),shadow_color=(255,0,0),shadow=True)
about_menu.add_image('rake.png', scale=(0.23, 0.23), scale_smooth=True)
about_menu.add_vertical_margin(50)
about_menu.add_label('Iztay Almaz',font_color=(0,252,255),shadow_color=(255,0,0),shadow=True)
about_menu.add_image('aleke.png',  scale=(1, 1))
about_menu.add_vertical_margin(50)
about_menu.add_label('Igen Arystan',font_color=(0,252,255),shadow_color=(255,0,0),shadow=True)
about_menu.add_image('areke.jpg',angle=90,  scale=(0.15, 0.15), scale_smooth=True)
about_menu.add_vertical_margin(50)
about_menu.add_label('Zhenis Nursultan',font_color=(0,252,255),shadow_color=(255,0,0),shadow=True)
about_menu.add_image('nureke.png',  scale=(0.3, 0.3), scale_smooth=True)

color_menu = pygame_menu.Menu(600, 800, "HERO", theme=mytheme)
menu.add_button(color_menu.get_title(), color_menu, font_color=(0,252,255),shadow_color=(255,0,0),shadow=True,
                background_color=(0,0,0,0))
color_menu.set_sound(engine, recursive=True)
# color_menu.add_button(' Серый ', pygame_menu.events.BACK,shadow=True,shadow_color=(0, 0, 100), background_color=(255,255,255))
# color_menu.add_button(' Зеленый ', pygame_menu.events.BACK,shadow=True,shadow_color=(0, 0, 100), background_color=(255,255,255))
color_menu.add_button(' BLUE ', pygame_menu.events.BACK, font_color=(0,0,255),shadow_color=(0,0,255),font_size=50,shadow=True,
                      background_color=(0,0,0,0))
red_menu = pygame_menu.Menu(600, 800, "RED", theme=mytheme)
color_menu.add_button(red_menu.get_title(), red_menu, font_size=50,font_color=(255,0,0),shadow_color=(0,0,0),shadow=True,background_color=(0,0,0,0))
red_menu.add_label('other colors will be ',font_color=(0,0,0,0),font_size=20,shadow_color=(255,255,255),shadow=True)
red_menu.add_vertical_margin(8)
red_menu.add_label(' available in version',font_color=(0,0,0,0),font_size=20,shadow_color=(255,255,255),shadow=True)
red_menu.add_vertical_margin(8)
red_menu.add_label('   23430 ',font_color=(0,0,0,0),font_size=20,shadow_color=(255,255,255),shadow=True)

rules_menu = pygame_menu.Menu(600, 800, "RULES", theme=mytheme)
menu.add_button(rules_menu.get_title(), rules_menu, font_color=(0,252,255),shadow_color=(255,0,0),shadow=True,background_color=(0,0,0,0))

rules_menu.add_label('Moving',font_color=(0,252,255),shadow_color=(255,0,0),shadow=True,margin=(-200,0))
rules_menu.add_vertical_margin(-100)
rules_menu.add_image('mm.png',  scale=(0.15, 0.15),margin=(0,0))

rules_menu.add_label('shooting',font_color=(0,252,255),shadow_color=(255,0,0),shadow=True,margin=(-200,0))
rules_menu.add_vertical_margin(-40)
rules_menu.add_image('space-key.png',  scale=(0.20, 0.20),margin=(50,0))


#color_menu.add_label('other colors will be ',font_color=(0,0,0,0),font_size=20,shadow_color=(255,255,255),shadow=True)
#about_menu.add_vertical_margin(8)
#color_menu.add_label(' available in version',font_color=(0,0,0,0),font_size=20,shadow_color=(255,255,255),shadow=True)
#about_menu.add_vertical_margin(8)
#color_menu.add_label('   23430 ',font_color=(0,0,0,0),font_size=20,shadow_color=(255,255,255),shadow=True)
menu.add_label(HELP, max_char=-1, font_size=15, margin=(1, 0),font_color=(0,252,255),shadow_color=(255,0,0),shadow=True)
menu.add_vertical_margin(15)
menu.add_button(' EXIT ', pygame_menu.events.EXIT,font_size=40,font_color=(255,0,0),shadow_color=(0,0,0,0),shadow=True,background_color=(0,0,0,0))
menu.mainloop(surface)

