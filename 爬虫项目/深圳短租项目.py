from selenium import webdriver
import time

fp=webdriver.ChromeOptions()
fp.add_experimental_option('prefs',{'profile.default_content_setting_values':{'images':2},'permissions.default.stylesheet':2,'javascript':2})
fp.add_argument('User-Agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36')
driver=webdriver.Chrome(options=fp)

for i in range(5):
    link="https://zh.airbnb.com/s/Shenzhen--China/homes?"+"items_offset="+str(i*20)
    driver.get(link)
    driver.implicitly_wait(10)
    time.sleep(2)
    # 隐形等待

    rent_list=driver.find_elements_by_css_selector('div._gig1e7')
    # 所有的出租房，注意这是个列表

    # print(rent_list)
    for each_house in rent_list:
        price=each_house.find_element_by_css_selector('div._1ixtnfc')
        price=price.text
        name=each_house.find_element_by_css_selector('div._qrfr9x5')
        name=name.text

        try:
            discount=each_house.find_element_by_css_selector('span._6vwvwy7').text
        except:
            discount='木有折扣'

        details=each_house.find_element_by_css_selector('div._wuffzwa').text

        print(price,name,discount,details)
    print('==================================================')
    time.sleep(2)