from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

# comment=driver.find_element_by_css_selector('div.reply-content')
# # 用CSS选择器查找元素
#
# content=comment.find_element_by_tag_name('p')
# # 通过元素的tag寻找
# print(content.text)

time.sleep(20)
# 网页加载太慢，需要给一个睡眠定时来等待加载后再抓取

#网页代码中的JavaScript解析成了一个iframe,所以我们找不到div.reply-content元素，需要加上iframe解析
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
comment=driver.find_element_by_xpath('/html/body/div/div[1]/div[9]/div[1]/div[2]/div[1]/div[1]')
# 由于CSS查找元素不唯一，所以无法定位，改用full xpath方式成功

content=comment.find_element_by_tag_name('p')
print(content.text)

