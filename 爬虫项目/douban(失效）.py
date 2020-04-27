import re
import urllib.request
import http.cookiejar as coo
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

loginurl = 'https://www.douban.com/accounts/login'
cookie = coo.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

data = {
    "form_email": "your email",
    "form_password": "your password",
    "source": "index_nav"
}
data = {}
data['form_email'] = '你的账号'
data['form_password'] = '你的密码'
data['source'] = 'index_nav'

response = opener.open(loginurl, urllib.parse.urlencode(data).encode('utf-8'))

# 验证成功跳转至登录页
if response.geturl() == "https://www.douban.com/accounts/login":
    html = response.read().decode()

    # 验证码图片地址
    imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url = imgurl.group(1)
        # 将验证码图片保存至同目录下
        res = urllib.request.urlretrieve(url, 'v.jpg')

        # 获取captcha-id参数
        captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>', html)

        if captcha:
            vcode = input('请输入图片上的验证码：')
            data["captcha-solution"] = vcode
            data["captcha-id"] = captcha.group(1)
            data["user_login"] = "登录"

            # 提交验证码验证
            response = opener.open(loginurl, urllib.parse.urlencode(data).encode('utf-8'))

            # 登录成功跳转至首页 '''
            if response.geturl() == "http://www.douban.com/":
                print('登录成功！')
