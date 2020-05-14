import pygame
from pygame.locals import *
from random import *


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load('images/enemy1.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.destroy_images=[]
        self.destroy_images.extend([
            pygame.image.load('images/enemy1_down1.png').convert_alpha(),
            pygame.image.load('images/enemy1_down2.png').convert_alpha(),
            pygame.image.load('images/enemy1_down3.png').convert_alpha(),
            pygame.image.load('images/enemy1_down4.png').convert_alpha()
        ])
        # 小飞机毁灭的四张过程图

        self.speed=2
        self.active=True
        self.mask=pygame.mask.from_surface(self.image)
        # 完美碰撞检测(将图片非透明部分设为mask)
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-5*self.height,0)
        # 生成小飞机位置从屏幕之上五行位置开始，这样就不会都在一排了

    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
        # 如果小飞机飞过屏幕，调用reset(),继续生成

    def reset(self):
        self.active=True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-5 * self.height, 0)


class MidEnemy(pygame.sprite.Sprite):
    energy=8
    # 因为不仅在这个__init__里要用到，所以在这里定义(全局变量）
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load('images/enemy2.png').convert_alpha()
        self.image_hit=pygame.image.load('images/enemy2_hit.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy2_down1.png').convert_alpha(),
            pygame.image.load('images/enemy2_down2.png').convert_alpha(),
            pygame.image.load('images/enemy2_down3.png').convert_alpha(),
            pygame.image.load('images/enemy2_down4.png').convert_alpha()
        ])
        # 中飞机毁灭的四张过程图

        self.speed=1
        self.active=True
        self.mask=pygame.mask.from_surface(self.image)
        # 完美碰撞检测(将图片非透明部分设为mask)
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-10*self.height,-self.height)
        # 中型飞机随机范围加大，而且第一轮不会出现

        self.energy=MidEnemy.energy
        self.hit=False
        # 定义一个判断击中属性

    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
        # 如果小飞机飞过屏幕，调用reset(),继续生成

    def reset(self):
        self.active=True
        self.energy=MidEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-10 * self.height, -self.height)


class BigEnemy(pygame.sprite.Sprite):
    energy = 20
    # 因为不仅在这个__init__里要用到，所以在这里定义(全局变量）
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1=pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2=pygame.image.load('images/enemy3_n2.png').convert_alpha()
        self.image_hit=pygame.image.load('images/enemy3_hit.png').convert_alpha()
        self.rect=self.image1.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/enemy3_down1.png').convert_alpha(),
            pygame.image.load('images/enemy3_down2.png').convert_alpha(),
            pygame.image.load('images/enemy3_down3.png').convert_alpha(),
            pygame.image.load('images/enemy3_down4.png').convert_alpha(),
            pygame.image.load('images/enemy3_down5.png').convert_alpha(),
            pygame.image.load('images/enemy3_down6.png').convert_alpha()
        ])
        # 小飞机毁灭的四张过程图

        self.speed=1
        self.active=True
        self.mask=pygame.mask.from_surface(self.image1)
        # 完美碰撞检测(将图片非透明部分设为mask)
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),\
                                     randint(-15*self.height,-5*self.height)
        # 大型飞机随机范围加大，而且前5轮不会出现

        self.energy=BigEnemy.energy
        self.hit = False
        # 定义一个判断击中属性

    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
        # 如果小飞机飞过屏幕，调用reset(),继续生成

    def reset(self):
        self.active=True
        self.energy=BigEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-15 * self.height, -5*self.height)
