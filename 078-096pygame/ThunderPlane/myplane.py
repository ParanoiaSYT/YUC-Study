import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1=pygame.image.load('images/me1.png').convert_alpha()
        self.image2=pygame.image.load('images/me2.png').convert_alpha()
        self.rect=self.image1.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.rect.left,self.rect.top=(self.width-self.rect.width)//2,\
                                     self.height-self.rect.height-60
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/me_destroy_1.png').convert_alpha(),
            pygame.image.load('images/me_destroy_2.png').convert_alpha(),
            pygame.image.load('images/me_destroy_3.png').convert_alpha(),
            pygame.image.load('images/me_destroy_4.png').convert_alpha()
        ])
        # 我方飞机毁灭时的四张过程图片列表

        self.active=True
        # 存活判断

        self.invincible=False
        # 设置初始无敌状态

        self.mask=pygame.mask.from_surface(self.image1)
        # 完美碰撞检测(将图片非透明部分设为mask)

        # 飞机速度设为10
        self.speed=10

# 定义四个移动方法
    def moveup(self):
        if self.rect.top>0:
            self.rect.top-=self.speed
        else:
            self.rect.top=0
    def movedown(self):
        if self.rect.bottom<self.height-60:
            self.rect.top+=self.speed
        else:
            self.rect.bottom=self.height-60
    def moveleft(self):
        if self.rect.left>0:
            self.rect.left-=self.speed
        else:
            self.rect.left=0
    def moveright(self):
        if self.rect.right<self.width:
            self.rect.left+=self.speed
        else:
            self.rect.right=self.width

    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, \
                                        self.height - self.rect.height - 60
        self.active=True
        self.invincible=True



# 检测按键有两种方法
# 一、event事件检测key（适用于不是特别频繁的情况）
# 二、Key模块，检测键盘事件序列，返回布尔类型(适用于频繁情况）



