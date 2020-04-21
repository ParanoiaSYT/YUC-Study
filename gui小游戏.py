Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:39:00) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import easygui as g
import sys
g.msgbox('嗨，欢迎进入SYT设计的第一个小游戏hhh')
while 1:
    msg='请问你希望在学校学到什么知识呢？'
    title='小游戏互动'
    choices=['谈恋爱','python','琴棋书画']

    choices=g.choicebox(msg,title,choices)

    g.msgbox("你的选择是："+str(choices),"结果")

    if str(choices)=='谈恋爱':
        g.msgbox('年纪轻轻谈什么恋爱？？？')
    if str(choices)=='python':
        g.msgbox('有志气啊！！！')
    if str(choices)=='琴棋书画':
        g.msgbox('教不了你啊啊啊～')

    msg="你希望重新开始游戏吗？"
    title="请选择"

    if g.ccbox(msg,title):      #continue/cancel
        pass        #用户选择continue
    else:
        sys.exit(0)     #用户选择cancel
