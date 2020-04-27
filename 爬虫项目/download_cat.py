import urllib.request
import easygui as g

title='下载一只喵'
msg='请填写喵的尺寸'
fieldNames=['宽：','高：']
fieldValue=[]
fieldValue=g.multenterbox(msg,title,fieldNames)

while True:
    if fieldValue== None:       #加上这两句，点击cancel才能退出
        break
    errmsg =""
    try:
        width = int(fieldValue[0].strip())
    except:
        errmsg += "宽度必须为整数！"

    try:
        height = int(fieldValue[1].strip())
    except:
        errmsg += "高度必须为整数！"
    if errmsg =="":
        break
    fieldValue =[]
    fieldValue = g.multenterbox(errmsg, title, fieldNames, fieldValue)

response=urllib.request.urlopen("http://placekitten.com/%d/%d"%(width,height))
cat_img=response.read()

# with open('cat_800*800.jpg','wb') as f:         #图片也是二进制文件
#     f.write(cat_img)

file_path=g.filesavebox(default='*.jpg')
with open(file_path,'wb')as f:
    f.write(cat_img)
