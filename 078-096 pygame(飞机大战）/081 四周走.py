import pygame
import sys
from pygame.locals import *


pygame.init()
#实例化一个Clock对象(调整游戏帧率）
clock=pygame.time.Clock()

speed = [10, 5]  # 横向速度2，纵向速度1 (像素点）
bg=(255,255,255)    #显示RGB白色
size=width,height=1200,800
fullscreen=False

print(pygame.display.list_modes())  #显示当前显示器支持的尺寸

screen=pygame.display.set_mode(size,RESIZABLE)
pygame.display.set_caption("这是我的第一个pygame小游戏")

osheep=pygame.image.load("timg.jpeg").convert()
sheep=osheep

# 设置放大缩小的比率
radio=1.0

o_rect=osheep.get_rect()
position=sheep_rect=osheep.get_rect()

sheep_right=pygame.transform.rotate(sheep,90)
sheep_top=pygame.transform.rotate(sheep,180)
sheep_left=pygame.transform.rotate(sheep,270)
sheep_bottom=sheep

sheep=sheep_top
# 定义头部朝向
l_head=pygame.transform.flip(sheep,True,False)
r_head=sheep

while True:
    # 设置系统退出方式
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 如果发生了窗口关闭事件,就会引发系统的关闭

# 受控设置
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-20, 0]
                sheep=l_head
            elif event.key == pygame.K_RIGHT:
                speed = [20, 0]
                sheep=r_head
            elif event.key == pygame.K_UP:
                speed = [0, -20]
            elif event.key == pygame.K_DOWN:
                speed = [0, 20]

    # 全屏设置(F11)
            elif event.key==pygame.K_F12:
                fullscreen=not fullscreen
                if fullscreen:
                    size=width,height=pygame.display.list_modes()[0]
                # 获得当前浏览器所支持的最大尺寸
                    screen=pygame.display.set_mode(size,FULLSCREEN|HWSURFACE)
                # 第一个参数是显示屏尺寸,第二个是全屏｜硬件加速
                else:
                    size=width,height=1200,800
                    screen=pygame.display.set_mode(size,RESIZABLE)

            # 放大、缩小懒羊羊（+-),空格恢复原始尺寸
            if event.key==pygame.K_EQUALS or event.key==pygame.K_MINUS or event.key==pygame.K_SPACE:
                # 最大只能放大一倍，缩小50%
                if event.key==pygame.K_EQUALS and radio<2.0:
                    radio+=0.1
                if event.key==K_MINUS and radio>0.5:
                    radio-=0.1
                if event.key==K_SPACE:
                    radio=1.0

                sheep=pygame.transform.smoothscale(osheep,(int(o_rect.width*radio),int(o_rect.height*radio)))
    # smoothscale精准变换,尺寸需要整型来显示(osheep作为一个标准模型,每次按比率变换sheep）

                l_head = pygame.transform.flip(sheep, True, False)
                r_head = sheep
                if speed[0]<0:
                    sheep=l_head
                else:
                    sheep=r_head

    if position.right>width:
        sheep=sheep_right
        position=sheep_rect=sheep.get_rect()
        position.right=width    #贴边
        speed=[0,5]
    if position.bottom>height:
            sheep=sheep_bottom
            position=sheep_rect=sheep.get_rect()
            position.bottom=height    #贴边
            position.right=width
            speed=[-5,0]
    if position.left<0:
            sheep=sheep_left
            position=sheep_rect=sheep.get_rect()
            position.left=0    #贴边
            position.bottom=height
            speed=[0,-5]
    if position.top<0:
            sheep=sheep_top
            position=sheep_rect=sheep.get_rect()
            position.top=0    #贴边
            speed=[5,0]

    position=position.move(speed)

    screen.fill(bg)
    # 更新图片及位置、大小(将新图像画上去）
    screen.blit(sheep,position)

    # 更新界面(刷新）(双缓冲模式,新图换旧图）,将贴好新图的画面呈现出来
    pygame.display.flip()
    pygame.time.delay(10)

    clock.tick(60)     #设置帧率
