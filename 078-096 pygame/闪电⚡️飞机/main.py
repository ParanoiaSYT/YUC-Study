import pygame
import sys
from pygame.locals import *
import traceback
import myplane
import enemy




pygame.init()
pygame.mixer.init()

bg_size=width,height=480,700
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption("闪电⚡️飞机")

background=pygame.image.load('images/background.png').convert()

# 载入游戏音乐
# bgm
pygame.mixer.music.load('sound/game_music.ogg')
pygame.mixer.music.set_volume(0.2)
# 各种sound
bullet_sound=pygame.mixer.Sound('sound/bullet.wav')
bullet_sound.set_volume(0.2)
bomb_sound=pygame.mixer.Sound('sound/use_bomb.wav')
bomb_sound.set_volume(0.2)
supply_sound=pygame.mixer.Sound('sound/supply.wav')
supply_sound.set_volume(0.2)
get_bomb_sound=pygame.mixer.Sound('sound/get_bomb.wav')
get_bomb_sound.set_volume(0.2)
get_bullet_sound=pygame.mixer.Sound('sound/get_bullet.wav')
get_bullet_sound.set_volume(0.2)
upgrade_sound=pygame.mixer.Sound('sound/upgrade.wav')
upgrade_sound.set_volume(0.2)
enemy3_fly_sound=pygame.mixer.Sound('sound/enemy3_flying.wav')
enemy3_fly_sound.set_volume(0.2)
enemy3_down_sound=pygame.mixer.Sound('sound/enemy3_down.wav')
enemy3_down_sound.set_volume(0.5)
enemy2_down_sound=pygame.mixer.Sound('sound/enemy2_down.wav')
enemy2_down_sound.set_volume(0.2)
enemy1_down_sound=pygame.mixer.Sound('sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.1)
me_down_sound=pygame.mixer.Sound('sound/me_down.wav')
me_down_sound.set_volume(0.2)


def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2=enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)
def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3=enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)



def main():
    pygame.mixer.music.play(-1)
    # 这里参数-1是指无限循环播放bgm

    # 生成我方飞机,调用myplane模块的MyPlace实例化
    me =myplane.MyPlane(bg_size)
    # 用于切换飞机尾气图片
    switch_image=True
    # 用于延迟
    delay=100

    # 生成敌方飞机(将所有敌机放入碰撞组）
    enemies=pygame.sprite.Group()
    # 除了所有飞机一个组，不同种类的飞机也各自有组
    # 生成敌方小飞机
    small_enemies=pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)
    # 生成敌方中飞机
    mid_enemies=pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,4)
    # 生成敌方大飞机
    big_enemies=pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)

    # 中弹图片索引
    e1_destroy_index=0
    e2_destroy_index=0
    e3_destroy_index=0
    me_destroy_index=0


    clock=pygame.time.Clock()
    running=True

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        # key模块 检测用户的整个键盘操作，返回布尔类型值
        key_pressed=pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveup()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.movedown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveleft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveright()


        # 背景绘制
        screen.blit(background,(0,0))

        # 绘制大飞机
        for each in big_enemies:
            if each.active:
                each.move()
                if switch_image:
                    screen.blit(each.image1,each.rect)
                else:
                    screen.blit(each.image2,each.rect)
            # 大飞机即将出现时带音效
                if each.rect.bottom==-50:
                    # 大飞机speed=1，肯定会到达-50,这时候开始播放(知道挂掉）
                    enemy3_fly_sound.play(-1)
                    # -1表示循环播放
            else:
                if not (delay%3):
                    # 降速否则毁灭图片看不清
                    if e3_destroy_index == 0:
                        # 毁灭之歌
                        enemy3_down_sound.play()
                    # 毁灭时放图片（索引）
                    screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                    # 下面是个小技巧，余数从0～5，对应毁灭图片列表里6歌元素
                    e3_destroy_index=(e3_destroy_index+1)%6
                    # 一开始（0+1）%6==1 ，下面判断确保进行一轮
                    if e3_destroy_index==0:
                        enemy3_fly_sound.stop()
                        each.reset()

        # 绘制中飞机
        for each in mid_enemies:
            if each.active:
                each.move()
                screen.blit(each.image,each.rect)
            else:
                if not (delay % 3):
                # 降速否则毁灭图片看不清
                    if e2_destroy_index == 0:
                        # 毁灭之歌
                        enemy2_down_sound.play()
                        # 防止pygame音效通道被占满（防止重复帧播放音效）
                    # 毁灭时放图片（索引）
                    screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                    # 下面是个小技巧，余数从0～5，对应毁灭图片列表里6歌元素
                    e2_destroy_index=(e2_destroy_index+1)%4
                    # 一开始（0+1）%6==1 ，下面判断确保进行一轮
                    if e2_destroy_index==0:
                        each.reset()

         # 绘制小飞机
        for each in small_enemies:
            if each.active:
                each.move()
                screen.blit(each.image,each.rect)
            else:
                if not (delay % 3):
                # 降速否则毁灭图片看不清
                    if e1_destroy_index==0:
                        # 毁灭之歌
                        enemy1_down_sound.play()
                    # 毁灭时放图片（索引）
                    screen.blit(each.destroy_images[e1_destroy_index],each.rect)
                    # 下面是个小技巧，余数从0～5，对应毁灭图片列表里6歌元素
                    e1_destroy_index=(e1_destroy_index+1)%4
                    # 一开始（0+1）%6==1 ，下面判断确保进行一轮
                    if e1_destroy_index==0:
                        each.reset()

        #检测我方飞机是否被撞（第三个参数是碰撞毁灭False,第四个参数默认是矩形区域检测））
        enemies_down=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)
        # pygame.sprite.collide_mask图片非透明部分接触碰撞
        if enemies_down:
            me.active=False
        # 返回一个列表，里面包含所有与sprite碰撞的元素,敌机的active也为False
            for e in enemies_down:
                e.active=False



        # 我方飞机绘制(尾气切换)
        if me.active:
            if switch_image:
                screen.blit(me.image1,me.rect)
            else:
                screen.blit(me.image2,me.rect)
        else:
            if not (delay % 3):
            # 降速否则毁灭图片看不清
                if me_destroy_index == 0:
                    # 毁灭之歌
                    me_down_sound.play()
                # 毁灭时放图片（索引）
                screen.blit(me.destroy_images[me_destroy_index], me.rect)
                # 下面是个小技巧，余数从0～5，对应毁灭图片列表里6歌元素
                me_destroy_index = (me_destroy_index + 1) % 4
                # 一开始（0+1）%6==1 ，下面判断确保进行一轮
                if me_destroy_index == 0:
                    # me.reset()
                    print("GAME OVER")
                    running=False

        # 延迟切换(delay只有被5整除的时候才会切换)
        if not(delay%5):
            switch_image = not switch_image
        delay-=1
        if not delay:
            delay=100
        # 相当于60帧的游戏尾气切换只有12帧


        pygame.display.flip()
        clock.tick(60)

if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
    # 如果是系统退出，即正常退出就pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
        # input起到一个停留的作用（接受用户输入才可以走）(聚焦作用）
