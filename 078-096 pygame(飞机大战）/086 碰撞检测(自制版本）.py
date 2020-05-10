import pygame
import sys
from pygame.locals import *
from random import *
import math


class Ball(pygame.sprite.Sprite):
    # pygame.sprite.Sprite是pygame里精灵的基类，继承就行

    def __init__(self,image,position,speed,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(image).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.speed=speed
        self.width,self.height=bg_size[0],bg_size[1]

    def move(self):
        self.rect=self.rect.move(self.speed)
        #这里用rect的move方法就可以了

        # 设置小球碰左墙后从相连右边出来(穿越效果)
        if self.rect.right<0:
            self.rect.left=self.width
        elif self.rect.left>self.width:
            self.rect.right=0
        elif self.rect.bottom<0:
            self.top=self.height
        elif self.rect.top>self.height:
            self.rect.bottom=0

def collide_check(item,target):
    col_balls=[]
    for each in target:
        distance=math.sqrt(math.pow((item.rect.center[0]-each.rect.center[0]),2)
                           +math.pow((item.rect.center[1]-each.rect.center[1]),2))
        if distance<=(item.rect.width+each.rect.width)/2:
            col_balls.append(each)
    return col_balls


def main():
    pygame.init()

    bg_size=width,height=1024,681
    screen=pygame.display.set_mode(bg_size)
    pygame.display.set_caption("玩球")

    ball_image = 'gray_ball.png'
    bg_image = 'background.png'
    background = pygame.image.load(bg_image).convert_alpha()

    running = True

    # 创建五个随机小球放入balls列表
    balls=[]
    BALL_NUM=5
    for i in range(BALL_NUM):
        position=randint(0,width-100),randint(0,height-100)
        # 球的直径为100
        speed=[randint(-10,10),randint(-10,10)]
        ball=Ball(ball_image,position,speed,bg_size)
        # Ball类实例化
        while collide_check(ball,balls):
            ball.rect.left,ball.rect.top=randint(0,width-100),randint(0,height-100)
        balls.append(ball)

    clock=pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        screen.blit(background,(0,0))

        for each_ball in balls:
            each_ball.move()
            screen.blit(each_ball.image,each_ball.rect)
            # class Ball里传入的rect就是矩形位置

        for i in range(BALL_NUM):
            item=balls.pop(i)
            if collide_check(item,balls):
                item.speed[0]=-item.speed[0]
                item.speed[1]=-item.speed[1]

            balls.insert(i,item)
        #     pop取出后要记得再放进去

        pygame.display.flip()
        clock.tick(30)




if __name__=='__main__':
    main()