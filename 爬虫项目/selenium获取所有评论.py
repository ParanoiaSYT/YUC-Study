from selenium import webdriver
import time

start=time.time()

# 控制CSS加载(限制CSS,图片和JAVAscript)
fp=webdriver.ChromeOptions()
prefs={'profile.default_content_setting_values':{'images':2},'permissions.default.stylesheet':2}       #来必力要求激活JAVAscript，{'javascript':2}
fp.add_experimental_option('prefs',prefs)
driver=webdriver.Chrome(options=fp)


driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(10)          #由于"来必力"加载太慢，只能暴力等待
# 隐形等待是设置了一个最长等待时间,如果在规定时间内网页加载完成,则执行下一步,否则一直等到时间截止,然后执行下一步.
# driver.implicitly_wait(20)

def print_eachpage():
    # driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
    comments=driver.find_elements_by_css_selector('div.reply-content')

    for each in comments:
        content=each.find_element_by_tag_name('p')
        print(content.text)

for i in range(0,3):
    # 下滑到页面底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    # 转换iframe
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
    # 再找到下一页点击

    next_page=driver.find_element_by_xpath("/html/body/div/div[1]/div[9]/div[12]/button[%d]"%(i+1))
    #⚠️注意这里在翻到第4页后，next_page的xpath最后一个为div[14]，非[12]，这里只打印了前三页的评论
    next_page.click()

    time.sleep(3)
    print_eachpage()
    # 再吧iframe转回去
    driver.switch_to.default_content()
    time.sleep(2)

finish=time.time()
print('总共运行时间为：%s秒'%str(finish-start))





