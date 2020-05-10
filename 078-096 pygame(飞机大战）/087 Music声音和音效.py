# pygame只支持OGG,wav格式
# 播放音效 pygame.mixer.Sound()
# 播放bgm pygame.mixer.music

import pygame
from pygame.locals import *
import sys


pygame.init()
# pygame.mixer.init()   #一般pygame初始化就会一起初始化了

pygame.mixer.music.load('Music/bg_music.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

cat_sound=pygame.mixer.Sound('Music/cat.wav')
cat_sound.set_volume(0.2)
dog_sound=pygame.mixer.Sound('Music/dog.wav')
dog_sound.set_volume(0.2)

bg_size=width,height=1024,681
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption("音乐🎵")

pause=False
background=pygame.image.load('background.png').convert_alpha()
pause_image=pygame.image.load('Music/pause.png').convert_alpha()
continue_image=pygame.image.load('Music/unpause.png').convert_alpha()
pause_rect=pause_image.get_rect()
continue_rect=continue_image.get_rect()
pause_rect.center=width//2,height//2
continue_rect.center=width//2,height//2

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                cat_sound.play()
            elif event.button==3:
            # pygame在Mac上右键事件是button==3
                dog_sound.play()
        elif event.type==KEYDOWN:
            if event.key==K_SPACE:
                pause=not pause


    screen.blit(background,(0,0))
    # screen.fill((255,255,255))

    if pause:
        screen.blit(pause_image,pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(continue_image,continue_rect)
        pygame.mixer.music.unpause()


    pygame.display.flip()
    clock.tick(60)
