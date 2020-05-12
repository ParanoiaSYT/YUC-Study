from PIL import Image
# pillow 是PIL的一个分支


img=Image.open("timg.jpeg")
out=img.convert("L")
# L表示灰度模式

out.show()

print(out.size)
width,height=out.size

out=out.resize((int(width*0.5),int(height/8)))
# 注意这里是个二元组
# 一般字符的高要比宽大不少，加上还有行距等等，自己改改比例
width,height=out.size
print(width,height)

# 获得指定位置的灰度参数值(0就是黑色，255就是白色)
# print(out.getpixel((100,100)))
print(out.getpixel((10,10)))

# 选一些ascii码(灰度越来越小，越来越白）
asciis="@&%#*+=-."
# texts用来存放数据，保存为文本文件
texts=''

for row in range(height):
    for col in range(width):
        gray=out.getpixel((col,row))
        # 获得灰度值
        texts+=asciis[int(gray/255 * 8)]
        # 进行归一（gray等于0就是0...等于255就是8）
    texts+='\n'

with open('ascii.txt','w')as f:
    f.write(texts)
