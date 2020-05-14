import pygame
import sys

pygame.init()

size=width,height=1200,800
screen=pygame.display.set_mode(size)
# 设置标题
pygame.display.set_caption("事件统计")
bg=(0,0,0)

font=pygame.font.Font(None,20)
# 第一个参数是字体(默认就是系统自带）,20是尺寸
screen.fill(bg)

positon=0
line_height=font.get_linesize()
# 获取行高(这个放不放在循环里都可以，会自动更新）

with open("record.txt","w")as f:
    while True:
        for event in pygame.event.get():
            # f.write(str(event)+'\n')

            if event.type==pygame.QUIT:
                sys.exit()

            a=font.render(str(event),True,(0,255,0))
            # 渲染成一个Surface对象（内容，是否消除锯齿，颜色）
            screen.blit(a,(0,positon))
            # 然后把渲染的对象在指定位置呈现出来
            positon+=line_height

            if positon>height:
                positon=0
                screen.fill(bg)

        pygame.display.flip()