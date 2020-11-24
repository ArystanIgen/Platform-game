from moviepy.editor import VideoFileClip
import pygame
from moviepy.video.fx.resize import resize
def qw():
    pygame.display.set_caption('God job!!!!')
    clip = VideoFileClip('level_complete.mp4')
    clip.resize(width=10)
    clip.preview()
    pygame.quit()
if __name__ == "__main__":
    qw()
