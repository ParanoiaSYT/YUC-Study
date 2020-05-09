import pygame
import sys
from pygame.locals import *
# 加上这句后就可以直接用函数名了


# 先初始化pygame
pygame.init()
#实例化一个Clock对象(调整游戏帧率）
clock=pygame.time.Clock()

speed = [10, 5]  # 横向速度2，纵向速度1 (像素点）
bg=(255,255,255)    #显示RGB白色
size=width,height=800,600
fullscreen=False

print(pygame.display.list_modes())  #显示当前显示器支持的尺寸

# 创建指定大小的窗口 返回一个Surface对象(pygame中用来表示图像的对象）
screen=pygame.display.set_mode(size,RESIZABLE)
# 设置窗口标题
pygame.display.set_caption("这是我的第一个pygame小游戏")

# 加载图片
picture=pygame.image.load("timg.jpeg").convert()
picture2=pygame.image.load("18.gif").convert()
picture2.set_alpha(100)
# 设置picture2的透明度（范围是0～255）2^8

# 获得图片的位置(矩形位置）
position=picture.get_rect()
position2=picture2.get_rect()
# rect()只有四个属性（left,top,width,height)

# 定义头部朝向
l_head=pygame.transform.flip(picture,True,False)
r_head=picture

while True:
    # 设置系统退出方式
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 如果发生了窗口关闭事件,就会引发系统的关闭

# 受控设置
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-5, 0]
                picture=l_head
            elif event.key == pygame.K_RIGHT:
                speed = [5, 0]
                picture=r_head
            elif event.key == pygame.K_UP:
                speed = [0, -5]
            elif event.key == pygame.K_DOWN:
                speed = [0, 5]
            # else:
            #     speed=[10,5]

    # 全屏设置(F11)
            elif event.key==pygame.K_F12:
                fullscreen=not fullscreen
                if fullscreen:
                    size=width,height=pygame.display.list_modes()[0]
                # 获得当前浏览器所支持的最大尺寸
                    screen=pygame.display.set_mode(size,FULLSCREEN|HWSURFACE)
                # 第一个参数是显示屏尺寸,第二个是全屏｜硬件加速
                else:
                    size=width,height=800,600
                    screen=pygame.display.set_mode(size,RESIZABLE)

    # # 用户调整窗口尺寸(加不加好像没有区别,更新后自动了？）
    #     if event.type==VIDEORESIZE:
    #         width,height=size=event.size

    # 移动图片
    position=position.move(speed)

# 触碰边界判断（左边界（0，0），右边界（width,height)
    # 横向边界判断
    if position.left < 0 or position.right>width:
        # 横向翻转图片（转向）三个参数为（目标，是否横翻，是否纵翻）
        picture=pygame.transform.flip(picture,True,False)
        # 横向速度变向
        speed[0]=-speed[0]
    # 纵向边界判断
    if position.top<0 or position.bottom>height:
        # 纵向速度变向
        speed[1]=-speed[1]

    # 填充背景(整个画面刷成白色)
    screen.fill(bg)
    # 更新图片及位置、大小(将新图像画上去）
    screen.blit(picture,position)
    screen.blit(picture2,position2)

    # 更新界面(刷新）(双缓冲模式,新图换旧图）,将贴好新图的画面呈现出来
    pygame.display.flip()
    # 延迟5ms（不然移动太快了）
    # pygame.time.delay(5)
    clock.tick(60)     #设置帧率
