import pygame
import sys
from pygame.locals import *

# surface的convert 是像素格式的转换
# blit会自动进行转换(图片黏贴时）,效率低下
# 包含alpha通道的图片通过convert_alpha()来转换
# jpg、jpeg格式不包含alpha通道,png、gif、tga、bmp都包含
# pygame中gif不能解析

# 三种方式设置alpha
# 1、set_colorkey((255,255,255))，只能消除某一种rgb颜色变为背景色
# 2、set_alpha(150) ,改变整个图片透明度
# 3、get_at((x,y)) 可以获得某个位置的rgba再改(前提要可以convert_alpha())

# 1、2可以混合使用，3不怎么用

pygame.init()

size=width,height=1280,720
bg=(0,0,0)

clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("alpha透明度测试")

sheep=pygame.image.load('timg.jpeg').convert()
background=pygame.image.load('background.jpeg').convert()

positon=sheep.get_rect()
positon.center=width//2,height//2
# sheep居中显示

sheep.set_colorkey((255,255,255)) #将sheep的某种颜色消除变为背景色
sheep.set_alpha(150)    #将整个sheep改变透明度,会显露背景



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen.blit(background,(0,0))
    screen.blit(sheep,positon)

    pygame.display.flip()

    clock.tick(30)

