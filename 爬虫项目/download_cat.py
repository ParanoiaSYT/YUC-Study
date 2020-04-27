import urllib.request

response=urllib.request.urlopen("http://placekitten.com/800/800")
cat_img=response.read()

with open('cat_800*800.jpg','wb') as f:         #图片也是二进制文件
    f.write(cat_img)

print(response.geturl())
print(response.info())
print(response.getcode())       #http的状态码，200表示正常响应