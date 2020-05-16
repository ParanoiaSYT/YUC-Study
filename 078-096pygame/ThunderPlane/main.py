import pygame
import sys
from pygame.locals import *
import traceback
import myplane
import enemy
import bullet
import supply
from random import *
import os



pygame.init()
pygame.mixer.init()

bg_size=width,height=640,880
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption("闪电⚡️战机")

background=pygame.image.load('images/background.png').convert_alpha()
thunder_image=pygame.image.load('images/thunder.png').convert()

# 定义颜色
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)

# 载入游戏音乐
# bgm
pygame.mixer.music.load(r'sound/game_music.ogg')
pygame.mixer.music.set_volume(0.15)
# 各种sound
bullet_sound=pygame.mixer.Sound(r'sound/bullet.wav')
bullet_sound.set_volume(0.1)
bomb_sound=pygame.mixer.Sound(r'sound/use_bomb.wav')
bomb_sound.set_volume(0.2)
supply_sound=pygame.mixer.Sound(r'sound/supply.wav')
supply_sound.set_volume(0.4)
get_bomb_sound=pygame.mixer.Sound(r'sound/get_bomb.wav')
get_bomb_sound.set_volume(0.2)
get_bullet_sound=pygame.mixer.Sound(r'sound/get_bullet.wav')
get_bullet_sound.set_volume(0.2)
upgrade_sound=pygame.mixer.Sound(r'sound/upgrade.wav')
upgrade_sound.set_volume(0.6)
enemy3_fly_sound=pygame.mixer.Sound(r'sound/enemy3_flying.wav')
enemy3_fly_sound.set_volume(0.2)
enemy3_down_sound=pygame.mixer.Sound(r'sound/enemy3_down.wav')
enemy3_down_sound.set_volume(0.5)
enemy2_down_sound=pygame.mixer.Sound(r'sound/enemy2_down.wav')
enemy2_down_sound.set_volume(0.2)
enemy1_down_sound=pygame.mixer.Sound(r'sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.1)
me_down_sound=pygame.mixer.Sound(r'sound/me_down.wav')
me_down_sound.set_volume(0.2)
thunder_sound=pygame.mixer.Sound('sound/thunder.wav')
thunder_sound.set_volume(0.6)

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
def increase_speed(target,inc):
    for each in target:
        each.speed+=inc

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

    # 生成普通子弹
    bullet1=[]
    bullet1_index=0
    BULLET1_NUM=6
    # 设置为四颗子弹（每屏幕）
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))
        # rect的midtop即位于顶部中央
    # 生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 12
    # 设置为四颗子弹（每屏幕）
    for i in range(BULLET2_NUM//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx-33,me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+30,me.rect.centery)))

    # 用于统计得分
    score=0
    score_font=pygame.font.Font('font/Herculanum.ttf',36)
    # pyinstaller打包时字体要写绝对路径

    # 暂停游戏标志
    paused=False
    paused_nor_image=pygame.image.load(r'./images/pause_nor.png').convert_alpha()
    paused_pressed_image=pygame.image.load(r'./images/pause_pressed.png').convert_alpha()
    resume_nor_image=pygame.image.load(r'./images/resume_nor.png').convert_alpha()
    resume_pressed_image=pygame.image.load(r'./images/resume_pressed.png').convert_alpha()
    paused_rect=paused_nor_image.get_rect()
    paused_rect.left,paused_rect.top=width-paused_rect.width-10,10
    paused_image=paused_nor_image
    # 设置暂停默认图片款式

    # 设置难度级别
    level=1

    # 设置全屏炸弹
    bomb_image=pygame.image.load(r'./images/bomb.png').convert_alpha()
    bomb_rect=bomb_image.get_rect()
    bomb_font=pygame.font.Font('font/Herculanum.ttf',48)
    bomb_num=3

    # 每30秒发放补给包
    bullet_supply=supply.Bullet_Supply(bg_size)
    bomb_supply=supply.Bomb_Supply(bg_size)
    # 补给包定时器(自定义事件） 30s
    SUPPLY_TIMER=USEREVENT
    pygame.time.set_timer(SUPPLY_TIMER,20*1000)


    # 超级子弹定时器
    DOUBLE_BULLET_TIMER=USEREVENT+1
    # 标志是否使用
    is_double_bullet=False

    #解除我方无敌计时器
    INVINCIBLE_TIMER=USEREVENT+2


    # 生命剩余
    life_image=pygame.image.load('images/life.png').convert_alpha()
    life_rect=life_image.get_rect()
    life_num=3

    # 用于阻止重复打开记录文件
    recorded=False

    # 游戏结束画面
    gameover_font=pygame.font.Font("font/Herculanum.ttf",48)
    again_image=pygame.image.load("images/again.png").convert_alpha()
    again_rect=again_image.get_rect()
    gameover_image=pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect=gameover_image.get_rect()


    # 中弹图片索引(中弹图片切换特效）
    e1_destroy_index=0
    e2_destroy_index=0
    e3_destroy_index=0
    me_destroy_index=0

    clock=pygame.time.Clock()
    running=True

    while running:
        # 偶尔发生的用event事件来描述即可
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1 and paused_rect.collidepoint(event.pos):
                    # rect的collidepoint方法检测事件是否发生的矩形区域内
                    paused=not paused
                    if paused:
                        # 暂停时音乐和音效暂停
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        #  音乐和音效继续播放
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()


            elif event.type==MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image=resume_pressed_image
                    else:
                        paused_image=paused_pressed_image
                else:
                    if paused:
                        paused_image=resume_nor_image
                    else:
                        paused_image=paused_nor_image
            elif event.type==KEYDOWN and not paused:
                if event.key==K_SPACE:
                    if bomb_num:
                        bomb_num-=1
                        thunder_sound.play()
                        screen.blit(thunder_image,(0,0))
                        pygame.display.flip()
                        pygame.time.delay(500)
                        for each in enemies:
                            if each.rect.bottom>0:
                                each.active=False
            elif event.type==SUPPLY_TIMER and not paused:
                supply_sound.play()
                if choice([True,False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            elif event.type==DOUBLE_BULLET_TIMER:
                # 触发超级子弹18秒后启动DOUBLE_BULLET_TIMER事件，定时器就关闭
                is_double_bullet=False
                pygame.time.set_timer(DOUBLE_BULLET_TIMER,0)
            elif event.type==INVINCIBLE_TIMER:
                me.invincible=False
                pygame.time.set_timer(INVINCIBLE_TIMER,0)
                # 触发解除无敌事件后，取消计时器



        # 根据用户得分增加难度
        if level==1 and score >500:
            level=2
            upgrade_sound.play()
            # 增加三架小飞机，两架中飞机,一架大飞机
            add_small_enemies(small_enemies,enemies,3)
            add_mid_enemies(mid_enemies,enemies,2)
            add_big_enemies(big_enemies,enemies,1)
            # 提升小飞机速度(1点）
            increase_speed(small_enemies,1)
        elif level==2 and score>2000:
            level=3
            upgrade_sound.play()
            # 增加三架小飞机，两架中飞机,一架大飞机
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            increase_speed(small_enemies, 1)
            increase_speed(mid_enemies, 1)
        elif level==3 and score>8000:
            level = 4
            upgrade_sound.play()
            # 增加三架小飞机，两架中飞机,一架大飞机
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            increase_speed(small_enemies, 1)
            increase_speed(mid_enemies, 1)
        elif level == 4 and score > 15000:
            level = 5
            upgrade_sound.play()
            # 增加三架小飞机，两架中飞机,一架大飞机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            increase_speed(small_enemies, 1)
            increase_speed(mid_enemies, 1)

        # 背景绘制
        screen.blit(background, (0, 0))

        if life_num and not paused:
            # 频繁发生的用key模块 检测用户的整个键盘操作，返回布尔类型值
            key_pressed=pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveup()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.movedown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveleft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveright()


            # 绘制炸弹补给包并检测获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image,bomb_supply.rect)
                if pygame.sprite.collide_mask(me,bomb_supply):
                    # 这里检测完美碰撞（两个单体），返回True和False
                    get_bomb_sound.play()
                    if bomb_num<3:
                        bomb_num+=1
                    bomb_supply.active=False
            # 绘制子弹补给包并检测获得
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(me, bullet_supply):
                    # 这里检测完美碰撞（两个单体），返回True和False
                    get_bullet_sound.play()
                    # 发射超级子弹,持续18秒
                    is_double_bullet=True
                    pygame.time.set_timer(DOUBLE_BULLET_TIMER,12*1000)
                    bullet_supply.active=False



            # 子弹发射（每10帧绘制一次）
            if not (delay%10):
                # 播放子弹声音
                bullet_sound.play()
                if is_double_bullet:
                    bullets=bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33,me.rect.centery))
                    bullets[bullet2_index+1].reset((me.rect.centerx+30,me.rect.centery))
                    # 传入二元组（位置)
                    bullet2_index=(bullet2_index+2)%BULLET2_NUM
                else:
                    bullets=bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    # 这里其实是预算了子弹差不多4颗能到屏幕80%地方(飞机下面状态栏占了20%）
                    bullet1_index=(bullet1_index+1)%BULLET1_NUM

            # 检测子弹是否击中敌机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image,b.rect)
                    enemy_hit=pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)
                    # 检测和敌机碰撞(返回碰撞敌机列表）
                    if enemy_hit:
                        b.active=False
                        for e in enemy_hit:
                            # 中飞机和大飞机血量为0才阵亡
                            if e in mid_enemies or e in big_enemies:
                                e.hit=True
                                e.energy-=1
                                if e.energy==0:
                                    e.active=False
                            else:
                                e.active = False

            # 绘制大飞机
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                    # 绘制被击中的特效
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:
                        if switch_image:
                            screen.blit(each.image1,each.rect)
                        else:
                            screen.blit(each.image2,each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen,BLACK,(each.rect.left,each.rect.top-5),(each.rect.right,each.rect.top-5),2)
                    # 在飞机上方五个像素位置画一条线(宽2像素）

                    # 当生命大于20%显示绿色，否则显示红色
                    energy_remanin=each.energy/enemy.BigEnemy.energy
                    if energy_remanin>0.2:
                        energy_color=GREEN
                    else:
                        energy_color=RED
                    pygame.draw.line(screen,energy_color,(int(each.rect.left),int(each.rect.top-5)),
                                     (int(each.rect.left)+int(each.rect.width*energy_remanin),int(each.rect.top-5)),2)
                    # 绘制生命剩余

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
                            score+=1000
                            each.reset()

            # 绘制中飞机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:
                        screen.blit(each.image,each.rect)
                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 2)
                    # 在飞机上方五个像素位置画一条线(宽2像素）

                    # 当生命大于20%显示绿色，否则显示红色
                    energy_remanin = each.energy / enemy.MidEnemy.energy
                    if energy_remanin > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, (int(each.rect.left), int(each.rect.top - 5)),
                                     (int(each.rect.left + each.rect.width * energy_remanin), int(each.rect.top - 5)), 2)
                    # 绘制生命剩余
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
                            score+=500
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
                            score+=100
                            each.reset()

            #检测我方飞机是否被撞（第三个参数是碰撞毁灭False,第四个参数默认是矩形区域检测））
            enemies_down=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)
            # pygame.sprite.collide_mask图片非透明部分接触碰撞
            if enemies_down and not me.invincible:
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
                        life_num-=1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIMER,3*1000)
                        # 设置reset后3秒，然后启动解除无敌状态

            # 得分显示(render函数将成字符串渲染成surface对象）
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            # 第二个参数为True表示拒绝锯齿
            screen.blit(score_text, (10, 5))


        # 生命为0结束
        elif life_num==0:
            # bgm停止
            pygame.mixer.music.stop()
            # 停止音效
            pygame.mixer.stop()
            # 停止补给包
            pygame.time.set_timer(SUPPLY_TIMER,0)

            if not recorded:
                # 读取历史最高分
                with open("record.txt",'a+')as f:
                    f.seek(0,0)
                    record_score=int(f.read())

                # 如果玩家得分高于最高分则存档
                    if score>record_score:
                        f.seek(0, 0)
                        f.truncate()
                        f.write(str(score))
                recorded=True
                print("Game Over!")
            #  绘制游戏结束画面
            record_score_text=score_font.render("Best : %d"%record_score,True,WHITE)
            screen.blit(record_score_text,(50,50))

            gameover_text1=gameover_font.render("Your Score",True,WHITE)
            gameover_text1_rect=gameover_text1.get_rect()
            gameover_text1_rect.left,gameover_text1_rect.top=(width-gameover_text1_rect.width)//2,height//3
            screen.blit(gameover_text1,gameover_text1_rect)

            # 分数显示
            gameover_text2=gameover_font.render(str(score),True,WHITE)
            gameover_text2_rect=gameover_text2.get_rect()
            gameover_text2_rect.left,gameover_text2_rect.top=(width-gameover_text2_rect.width)//2,gameover_text1_rect.bottom+10
            screen.blit(gameover_text2,gameover_text2_rect)

            # 重新开始按钮
            again_rect.left,again_rect.top=(width-again_rect.width)//2,gameover_text2_rect.bottom+50
            screen.blit(again_image,again_rect)

            # 游戏结束按钮
            gameover_rect.left,gameover_rect.top=(width-again_rect.width)//2,again_rect.bottom+10
            screen.blit(gameover_image,gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键(0表示第一个元素————鼠标左键）
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                        again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    main()
                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()



        # 绘制暂停按钮
        screen.blit(paused_image,paused_rect)

        # 绘制清屏炸弹显示
        # 炸弹图片
        screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
        # 炸弹文本
        bomb_text=bomb_font.render("x %d"%bomb_num,True,WHITE)
        text_rect=bomb_text.get_rect()
        screen.blit(bomb_text,(20+bomb_rect.width,height-5-text_rect.height))


        # 绘制生命剩余显示
        if life_num:
            for i in range(life_num):
                screen.blit(life_image,(width-10-(i+1)*life_rect.width,height-10-life_rect.height))


        # 延迟切换(delay只有被5整除的时候才会切换)
        if not(delay%5):
            switch_image = not switch_image
        delay-=1
        if not delay:
            delay=100
        # 相当于60帧的游戏尾气切换只有12帧


        pygame.display.flip()
        clock.tick(60)

# if __name__=='__main__':
#     try:
#         main()
#     except SystemExit:
#         pass
#     # 如果是系统退出，即正常退出就pass
#     except:
#         traceback.print_exc()
#         pygame.quit()
#         input()
#         # input起到一个停留的作用（接受用户输入才可以走）(聚焦作用）
main()