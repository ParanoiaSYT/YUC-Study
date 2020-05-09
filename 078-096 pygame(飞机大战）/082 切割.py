import pygame
import sys
from pygame.locals import *

pygame.init()


size=width,height=800,600
bg=(255,255,255)

clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

turtle=pygame.image.load("turtle.png")
positon=turtle.get_rect()
# 设置选择变量（0未选择，1选择中，2完成选择）
select=0
# 设置拖拽变量（0未拖拽，1拖拽中，2完成拖拽）
drag=0

select_rect=pygame.Rect(0,0,0,0)   #绘制矩形框(先初始化一个）

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        # 按键按下时
        elif event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                if select==0 and drag==0:
                # 获得鼠标的位置并放入
                    pos_start=event.pos
                    select=1
                elif select==2 and drag==0:
                    capture=screen.subsurface(select_rect).copy()
                # 获得一个子对象的矩形区域,复制一个为capture
                    capture_rect=capture.get_rect()
                    drag=1
                elif select==2 and drag==2:
                # 裁剪完再点击初始化
                    select=0
                    drag=0


# event.button时
        # 按键松开时
        elif event.type==MOUSEBUTTONUP:
            if event.button==1:
                # 选择ing，还没drag
                if select==1 and drag==0:
                    pos_stop=event.pos
                    select=2
                elif select==2 and drag==1:
                    drag=2

    screen.fill(bg)
    screen.blit(turtle,positon)

# 实时绘制矩形框
    if select:
        # mouse的get_pos()函数返回鼠标的位置（x,y)
        mouse_pos=pygame.mouse.get_pos()
        if select==1:
            pos_stop=mouse_pos

        select_rect.left,select_rect.top=pos_start
        select_rect.width,select_rect.height=(pos_stop[0]-pos_start[0]),(pos_stop[1]-pos_start[1])
        pygame.draw.rect(screen,(0,0,0),select_rect,1)
    # pygame绘画参数（在哪画surface，颜色，大小参数rect，线条宽度width=0表示填充）

    if drag:
        if drag==1:
        # 还在拖拽，矩形应随着鼠标的移动而移动
            capture_rect.center=mouse_pos
        screen.blit(capture,capture_rect)

    pygame.display.flip()
    clock.tick(60)


# 关于下面两句报错，对程序而已无关紧要，只不过是要把png24微换成png8位而已
# libpng warning: iCCP: known incorrect sRGB profile
# libpng warning: Interlace handling should be turned on when using png_read_image
