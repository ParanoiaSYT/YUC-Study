from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha


##################### 图片验证码

image=ImageCaptcha(fonts=['almfixed.ttf','Arimo-BoldItalic.ttf'])
# 添加想要的字体


image.write("FishC","captcha2.png")
# 第一个参数指定要写入的内容，第二个参数是名字



##################### 音频验证码
audio=AudioCaptcha(voicedir='dog.wav')
# 参数指定声音素材

audio.write("dog",'captcha.wav')


