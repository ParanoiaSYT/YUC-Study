import pygame
import sys
from pygame.locals import *
import math

pygame.init()

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)

points=[(400,375),(500,325),(600,375),(650,325),(650,425),(600,375),(500,425)]
points2=[(800,75),(900,25),(1000,75),(1050,25),(1050,125),(1000,75),(900,125)]


size=width,height=1280,720
screen=pygame.display.set_mode(size)
pygame.display.set_caption("简单图形绘制")

positon=size[0]//2,size[1]//2
moving=False

clock=pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:     # 1表示鼠标左键
                moving=True
        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                moving=False
    if moving:
        positon=pygame.mouse.get_pos()
    # 圆可以拖动
    screen.fill(WHITE)

    # 绘制矩形
    pygame.draw.rect(screen,BLACK,(50,50,150,50),0)
    pygame.draw.rect(screen,BLACK,(250,50,150,50),1)
    pygame.draw.rect(screen,BLACK,(450,50,150,50),10)
    #rect第一个参数是surface对象，第二个颜色，第三个参数是(left,top,width,height)，第四个是边框宽度（0就是填充）

    # 绘制多边形
    pygame.draw.polygon(screen,GREEN,points,0)
    # polygon第一个参数是surface对象，第二个颜色，第三个参数是包含各个顶点坐标的列表，第四个是边框宽度（0就是填充）

    # 绘制圆
    pygame.draw.circle(screen,RED,positon,30,2)
    pygame.draw.circle(screen,GREEN,positon,75,2)
    pygame.draw.circle(screen,BLUE,positon,120,2)
    # circle第一个参数是surface对象，第二个颜色，第三个参数是圆心坐标，第四个是半径,第五个是边框宽度（0就是填充）

    # 绘制椭圆
    pygame.draw.ellipse(screen,BLACK,(900,300,200,100),2)
    pygame.draw.ellipse(screen,BLACK,(1000,450,200,200),0)
    # ellipse第一个参数是surface对象，第二个颜色，第三个参数是指定限定矩形坐标，第四个是边框宽度（0就是填充）
    # 也可以通过椭圆来画圆

    # 绘制弧线
    pygame.draw.arc(screen,RED,(400,100,200,100),0,math.pi,1)
    pygame.draw.arc(screen,RED,(700,100,100,100),math.pi,0,1)
    # 也是通过限定矩形的方式来画的
    # arc（Surface,color,Rect,start_angle,stop_angle,width=1)
    # 弧线无法填充

    # 绘制线段
    # pygame.draw.lines(screen,BLUE,0,points2,2)
    pygame.draw.lines(screen,BLUE,1,points2,2)
    # 单条线段line(Surface, color, start_pos, end_pos, width)
    # 多条线段,closed参数为True就是首尾相连lines(Surface, color, closed, pointlist, width=1)
    # 注意这里的width设置为0没用，这也是和polygon区别

    # 抗锯齿线段(对比普通线段有一些阴影),相当于把周围的像素点附上阴影
    pygame.draw.line(screen,BLACK,(100,700),(400,550),1)
    pygame.draw.aaline(screen,BLACK,(75,700),(375,550),1)
    pygame.draw.aaline(screen,BLACK,(50,700),(325,550),0)
    # aaline(Surface, color, startpos, endpos, blend=1)
    # aalines(Surface, color, closed, pointlist, blend=1)
    # blend 参数指定是否通过绘制混合背景的阴影来实现抗锯齿功能,没有width参数所以只能绘制一个像素的线段

    pygame.display.flip()
    clock.tick(30)
