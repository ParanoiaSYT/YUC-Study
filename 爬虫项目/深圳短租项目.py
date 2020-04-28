from selenium import webdriver
import time

webdriver.ChromeOptions().add_argument('User-Agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36')
driver=webdriver.Chrome()
driver.get("https://zh.airbnb.com/s/Shenzhen--China/homes")
driver.implicitly_wait(10)
time.sleep(5)
rent_list=driver.find_elements_by_css_selector('div._gig1e7')
# 所有的出租房

# print(rent_list)
for each_house in rent_list:
    price=each_house.find_element_by_css_selector('div._1ixtnfc')
    price=price.text
    name=each_house.find_element_by_css_selector('div._qrfr9x5')
    name=name.text

    try:
        discount=each_house.find_element_by_css_selector('span._6vwvwy7').text
    except:
        discount='折扣在哪里？'

    details=each_house.find_element_by_css_selector('div._wuffzwa').text

    print(price,name,details,discount)

    time.sleep(2)