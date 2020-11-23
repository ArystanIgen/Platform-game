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
from pygame import mixer
import main
def menushka():
    pygame.init()  # инициализировал миксер
    mixer.music.load('jr.mp3')
    mixer.music.play(0, 20)  # loop
    pygame.mixer.music.set_volume(0.1)

    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'Mouse Click Fast.wav')

    FPS = 30.0
    H_SIZE = 600
    W_SIZE = 800
    pygame.init()
    HELP = " TROIA  TEAM"
    mytheme = pygame_menu.themes.Theme(background_color=(0, 0, 0, 0),  # transparent background
                    title_shadow=True,
                    title_background_color=(4, 47, 126))
    myimage = pygame_menu.baseimage.BaseImage(
        image_path='title2.png',
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    )
    mytheme.background_color = myimage
    surface = pygame.display.set_mode((800, 600))
    bg=pygame.image.load("title2.png")
    menu = pygame_menu.Menu(600, 800, 'STORM GLASS', theme=mytheme)
    menu.set_sound(engine, recursive=True)  # добавляем звук клика мыши в основное меню
    menu.add_text_input('Имя :', font_color=(0,252,255),shadow_color=(0,0,0),shadow=True, default='Игрок',background_color=(0, 0, 0,0))
    menu.add_button(' Начать ',main.main,font_color=(0,252,255),shadow_color=(0,0,0),shadow=True, background_color=(0,0,0,0))
    menu.add_button(' Выход ', pygame_menu.events.EXIT,font_color=(0,252,255),shadow_color=(0,0,0),shadow=True,background_color=(0,0,0,0))

    about_menu = pygame_menu.Menu(600, 800, "О нас", theme=mytheme)
    PATH = os.path.join(os.path.dirname(pygame_menu.__file__),
                        'resources', 'images', 'pygame_menu.png')
    menu.add_button(about_menu.get_title(), about_menu, font_color=(0,252,255),shadow_color=(0,0,0),shadow=True,background_color=(0,0,0,0))
    about_menu.add_image(PATH, angle=-10, scale=(0.15, 0.15), scale_smooth=True)
    about_menu.add_label('Tokumtayev Rakhat',font_color=(0,252,255),shadow_color=(0,0,0),shadow=True)
    about_menu.add_vertical_margin(50)
    about_menu.add_image(PATH, angle=10, scale=(0.15, 0.15))
    about_menu.add_label('Iztay Almaz',font_color=(0,252,255),shadow_color=(0,0,0),shadow=True)
    about_menu.add_vertical_margin(50)
    about_menu.add_image(PATH, angle=-10, scale=(0.15, 0.15), scale_smooth=True)
    about_menu.add_label('Igen Arystan',font_color=(0,252,255),shadow_color=(0,0,0),shadow=True)
    about_menu.add_vertical_margin(50)
    about_menu.add_image(PATH, angle=10, scale=(0.15, 0.15), scale_smooth=True)
    about_menu.add_label('Zhenis Nursultan',font_color=(0,252,255),shadow_color=(0,0,0),shadow=True)
    color_menu = pygame_menu.Menu(600, 800, "Персонаж", theme=mytheme)
    menu.add_button(color_menu.get_title(), color_menu, font_color=(0,252,255),shadow_color=(0,0,0),shadow=True,
                    background_color=(0,0,0,0))
    color_menu.set_sound(engine, recursive=True)
    # color_menu.add_button(' Красный ', pygame_menu.events.BACK,shadow=True ,shadow_color=(0, 0, 100),background_color=(255,255,255))
    # color_menu.add_button(' Серый ', pygame_menu.events.BACK,shadow=True,shadow_color=(0, 0, 100), background_color=(255,255,255))
    # color_menu.add_button(' Зеленый ', pygame_menu.events.BACK,shadow=True,shadow_color=(0, 0, 100), background_color=(255,255,255))
    color_menu.add_button(' Синий ', pygame_menu.events.BACK, font_color=(0,252,255),shadow_color=(0,0,0),shadow=True,
                          background_color=(0,0,0,0))
    color_menu.add_label('Другие цвета будут ',font_color=(0,252,255),shadow_color=(0,0,0),shadow=True)
    about_menu.add_vertical_margin(8)
    color_menu.add_label(' доступны в версии ',font_color=(0,252,255),shadow_color=(0,0,0),shadow=True)
    about_menu.add_vertical_margin(8)
    color_menu.add_label('  V 2.0 ',font_color=(0,252,255),shadow_color=(0,0,0),shadow=True)
    menu.add_label(HELP, max_char=-1, font_size=20, margin=(1, 0),font_color=(0,252,255),shadow_color=(0,0,0),shadow=True)
    menu.mainloop(surface)
if __name__ == "__main__":
    menushka()