from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
date : 2021/7/22
author : Yicheng
'''

# 初始化一个浏览器对象
bro = webdriver.Chrome("chromedriver.exe")
# 防检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

KEYWORD = 'ipad'

try:
    bro.get('https://www.taobao.com/')
    # wait = WebDriverWait(bro, 6)
    # input_area = wait.until(EC.presence_of_element_located(By.ID,'q'))
    # search_btn = wait.until(EC.presence_of_element_located('.btn-search'))
    sleep(3)
    input_area = bro.find_element_by_name('q')
    search_btn = bro.find_element_by_css_selector('.btn-search')
    print(input_area,search_btn)

    input_area.send_keys(KEYWORD)

    search_btn.click()

    sleep(2)
    login_blocks = bro.find_element_by_xpath('//div[@class="login-blocks"]/div[@class="alipay-login"]')

    login_blocks.click()


    sleep(15)



except Exception as e:
    print(e)


bro.quit()
