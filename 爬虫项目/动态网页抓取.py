import requests
import json

# link='https://api-zero.livere.com/v1/comments/list?callback=jQuery1124033509247768842676_1588041690456&limit=10&offset=1&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1588041690458'
# link2='https://api-zero.livere.com/v1/comments/list?callback=jQuery1124033509247768842676_1588041690456&limit=10&offset=2&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1588041690463'

def get_singlepage(link):

    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

    r=requests.get(link,headers=headers,timeout=10)
    # print(r.text)

    json_string=r.text
    json_string=json_string[json_string.find('{'):-2]       #json格式的内容从第一个大括号开始，结束于最后末尾的大括号（要去掉r.text最后的小括号和分号）

    target0=json.loads(json_string)
    print('=================================================')
    # print(target0)
    target=target0['results']['parents']
    print('=================================================')

    for each in target:
        message=each['content']
        print(message)

for page in range(1,10):
    link1='https://api-zero.livere.com/v1/comments/list?callback=jQuery1124033509247768842676_1588041690456&limit=10&offset='
    link2='&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1588041690463'
    link=link1+str(page)+link2
    print(link)
    get_singlepage(link)

# 每个评论页只有offset变了，link2最后的数字在google检查的时候显示各页虽然不同但是不重要，任选一个都可以连通