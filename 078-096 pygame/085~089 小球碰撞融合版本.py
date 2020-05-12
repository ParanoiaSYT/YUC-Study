import pygame
import sys
from pygame.locals import *
from random import *
import math
import traceback
# 异常捕获模块


# spritecollide(sprite,group,dokill,collided=None)
# 第三个参数是碰撞毁灭；第四个参数设置特殊检测方法，忽略的话默认检测rect
# 第四个参数pygame.sprite.collide_circle就是支持圆碰撞检测,但需要半径参数

class Ball(pygame.sprite.Sprite):
    # pygame.sprite.Sprite是pygame里精灵的基类，继承就行

    def __init__(self,grayball_image,greenball_image,position,speed,bg_size,target):
        pygame.sprite.Sprite.__init__(self)

        self.grayball_image=pygame.image.load(grayball_image).convert_alpha()
        self.greenball_image=pygame.image.load(greenball_image).convert_alpha()
        # 由于两小球尺寸一样,所以只要取灰球的rect位置即可
        self.rect=self.grayball_image.get_rect()
        # 小球初始位置
        self.rect.left,self.rect.top=position
        self.side=[choice([-1,1]),choice([-1,1])]
        # 小球运动的方向-1、1
        self.speed=speed
        # speed只描述速度大小
        self.collide=False
        # 添加是否碰撞标签
        self.target=target
        # control 控制变量(是否玩家控制）
        self.control=False
        self.width,self.height=bg_size[0],bg_size[1]
        self.radius=self.rect.width/2
        # 传入半径参数(圆碰撞检测所需)

    def move(self):
        if self.control:
            self.rect=self.rect.move(self.speed)
        else:
            self.rect=self.rect.move([self.side[0]*self.speed[0],
                                  self.side[1]*self.speed[1]])
        #这里用rect的move方法就可以了,不受控状态为矢量，

        # 设置小球碰左墙后从相连右边出来(穿越效果)
        if self.rect.right<=0:
            self.rect.left=self.width
        elif self.rect.left>=self.width:
            self.rect.right=0
        elif self.rect.bottom <= 0:
            self.rect.top = self.height
        elif self.rect.top>=self.height:
            self.rect.bottom=0


    # check方法检测在一秒内产生的事件数量是否匹配目标
    def check(self,motion):
        if self.target<motion<self.target+20:
            return True
        else:
            return False


class Glass(pygame.sprite.Sprite):
    # 定义一个玻璃面板类
    def __init__(self,glass_image,mouse_image,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.glass_image=pygame.image.load(glass_image).convert_alpha()
        self.glass_rect=self.glass_image.get_rect()
        self.glass_rect.left,self.glass_rect.top=(bg_size[0]-self.glass_rect.width)//2,\
                                                 bg_size[1]-self.glass_rect.height
        self.mouse_image=pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect=self.mouse_image.get_rect()
        self.mouse_rect.left,self.mouse_rect.top=self.glass_rect.left,self.glass_rect.top

        pygame.mouse.set_visible(False)
        # 鼠标不可见




def main():
    pygame.init()
    # pygame.mixer.init()

    grayball_image = 'gray_ball.png'
    greenball_image = 'green_ball.png'
    bg_image = 'background.png'
    glass_image='glass.png'
    mouse_image='mouse.png'

    running = True

    # 增加魔性BGM
    pygame.mixer.music.load('Music/bg_music.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

    # 添加音效
    loser_sound=pygame.mixer.Sound(r'Music/loser.wav')
    laugh_sound=pygame.mixer.Sound(r'Music/laugh.wav')
    winner_sound=pygame.mixer.Sound('Music/winner.wav')
    hole_sound=pygame.mixer.Sound(r'Music/hole.wav')

    # 音乐结束时游戏结束
    GAMEOVER=USEREVENT
    # USEREVENT表示24事件，24及以后都是自定义事件
    pygame.mixer.music.set_endevent(GAMEOVER)

    bg_size = width, height = 1024,681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("玩球")
    background = pygame.image.load(bg_image).convert_alpha()
    glass=Glass(glass_image,mouse_image,bg_size)

    # 创建一个motion变量来记录鼠标每一秒产生的事件数量
    motion=0
    MYTIMER=USEREVENT+1
    # USERVENT事件表示24（24以后的事件都是自定义）
    pygame.time.set_timer(MYTIMER,1*1000)
    # MYTIMER事件设定为1000ms

    # 每个黑洞的范围(含容错)(x1,x2,y1,y1)
    hole=[(116,120,198,202),(224,228,389,393),(502,506,319,323),
          (697,701,191,195),(905,909,418,422)]

    msgs=[]
    # 整一个要打印的列表

    # 创建五个随机小球放入balls列表
    balls=[]
    group=pygame.sprite.Group()

    BALL_NUM=5
    for i in range(BALL_NUM):
        position=randint(0,width-100),randint(0,height-100)
        # 球的直径为100
        speed=[randint(1,10),randint(1,10)]
        # 速度大小设置为1-10的随机
        ball=Ball(grayball_image,greenball_image,position,speed,bg_size,5*(i+1))
        # 这里设置target=5*(i+1)

        # Ball类实例化
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):
            ball.rect.left,ball.rect.top=randint(0,width-100),randint(0,height-100)
        balls.append(ball)
        group.add(ball)

    # 按下后100ms后开始，按键响应interval为100ms
    pygame.key.set_repeat(100,100)

    # 帧率实例化
    clock=pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                # 等2000ms（2s）
                laugh_sound.play()
                pygame.time.delay(3000)
                running=False
            # 如果满足自定义事件
            elif event.type==MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            # 检查motion量是否达标
                            each.speed=[0,0]
                            each.control=True
                    motion=0
            elif event.type==MOUSEMOTION:
                motion+=4

            # 如果小球受控,按下wasd会调节速度
            elif event.type==KEYDOWN:
                if event.key==K_w:
                    for each in group:
                        if each.control:
                            each.speed[1]-=1
                if event.key==K_s:
                    for each in group:
                        if each.control:
                            each.speed[1]+=1
                if event.key==K_a:
                    for each in group:
                        if each.control:
                            each.speed[0]-=1
                if event.key==K_d:
                    for each in group:
                        if each.control:
                            each.speed[0]+=1
            # 设置按键重复按下间隔（这样按住wasd可以持续加速）

                if event.key==K_SPACE:
                    for each in group:
                        if each.control:
                            for i in hole:
                                if i[0]<=each.rect.left<=i[1] and i[2]<=each.rect.top<=i[3]:
                                    hole_sound.play()
                                    each.speed=[0,0]
                                    group.remove(each)
                                    # 速度降为0，且each移除碰撞检测
                                    temp=balls.pop(balls.index(each))
                                    # 获得索引然后将其弹出另外绘制
                                    balls.insert(0,temp)
                                    # 弹出后插到第一个位置，这样就会再所有球前先绘制，在另外的下面
                                    hole.remove(i)
                            if not hole:
                                pygame.mixer.music.stop()
                                winner_sound.play()
                                pygame.time.delay(3000)
                                msg=pygame.image.load('msg.png').convert_alpha()
                                msg_pos=(width-msg.get_width())//2,(height-msg.get_height())//2
                                msgs.append((msg,msg_pos))
                                # 将要打印的内容和位置以元组形式加入列表中
                                laugh_sound.play()

        screen.blit(background,(0,0))
        screen.blit(glass.glass_image,glass.glass_rect)
        # 这里注意图层顺序，背景在最下面，glass在中间，小球在最上面

        # 限制鼠标不能出glass范围
        glass.mouse_rect.left,glass.mouse_rect.top=pygame.mouse.get_pos()
        if glass.mouse_rect.left<glass.glass_rect.left:
            glass.mouse_rect.left=glass.glass_rect.left
        if glass.mouse_rect.right>glass.glass_rect.right:
            glass.mouse_rect.right=glass.glass_rect.right
        if glass.mouse_rect.top<glass.glass_rect.top:
            glass.mouse_rect.top=glass.glass_rect.top
        if glass.mouse_rect.bottom>glass.glass_rect.bottom:
            glass.mouse_rect.bottom=glass.glass_rect.bottom

        screen.blit(glass.mouse_image,glass.mouse_rect)

        # 小球们移动并刷新画面
        for each_ball in balls:
            each_ball.move()
            if each_ball.collide:
                each_ball.speed = [randint(1, 10), randint(1, 10)]
                each_ball.collide=False
            if each_ball.control:
                # 控制变量为True就画绿色小球
                screen.blit(each_ball.greenball_image, each_ball.rect)
            else:
                screen.blit(each_ball.grayball_image, each_ball.rect)
            # class Ball里传入的rect就是矩形位置

        # 判断碰撞
        for each in group:
            group.remove(each)
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.side[0],each.side[1]=-each.side[0],-each.side[1]
                # 碰撞后速度的方向先反向
                each.collide=True

                if each.control:
                    each.side[0]=-1
                    each.side[1]=-1
                # 碰撞后取相反，即反向
                # 如果撞前是绿色可控的，那速度必然取反先（由矢量变标量）

                each.control=False
                # 一旦发生碰撞，小球就变不受控,控制变量取False
            group.add(each)

        for msg in msgs:
            screen.blit(msg[0],msg[1])
        # 每一个元素都是一个二元组


        pygame.display.flip()
        clock.tick(60)



if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()