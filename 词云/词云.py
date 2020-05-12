import wordcloud


with open('最多弹幕.txt') as f:
    text=f.read()

    stopword=['编程','教育','公开课','学习','课程','程序员','视频教程']
    # 加入词语黑名单
    wc=wordcloud.WordCloud(font_path='STSong.ttf',stopwords=stopword)
    # 实例化一个wordcloud对象,默认不支持中文，所以要加入中文字体



    wc.generate(text)
    # 这样就生成了一个词云

    image=wc.to_image()
    # 生成图像（通过pillow模块方法)

    image.show()