import pygame
import sys
from pygame.locals import *

pygame.init()

size=width,height=1280,720
bg=(0,0,0)

clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("alpha透明度测试")

turtle=pygame.image.load('turtle.png').convert_alpha()
background=pygame.image.load('background.jpeg').convert()

positon=turtle.get_rect()
print(turtle.get_at(positon.center))
# 打印出turtle中心处的rgba颜色，注意这句要在设置positon.center上面，否则指向的其实是画布上设置的positon.center位置(而不是图片中心）

positon.center=width//2,height//2
# sheep居中显示

turtle.set_alpha(50)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen.blit(background,(0,0))
    screen.blit(turtle,positon)

    pygame.display.flip()

    clock.tick(30)

