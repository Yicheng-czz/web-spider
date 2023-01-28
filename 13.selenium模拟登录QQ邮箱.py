from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

'''
date : 2021/7/22
author : Yicheng
'''

bro = webdriver.Chrome('chromedriver.exe')

QQ_zone = 'https://qzone.qq.com/'

bro.get(QQ_zone)
bro.switch_to.frame('login_frame')
up_btn = bro.find_element_by_id('switcher_plogin')
up_btn.click()

username = bro.find_element_by_id('u')
password = bro.find_element_by_id('p')

username.send_keys('1005383957')
sleep(2)
password.send_keys('QYCQyc1826784')
sleep(2)

login_btn = bro.find_element_by_id('login_button')

login_btn.click()
sleep(3)
# bro.switch_to.window()
bro.switch_to.frame('tcaptcha_iframe')


scroll = bro.find_element_by_id('tcaptcha_drag_thumb')

action = ActionChains(bro)
action.click_and_hold(scroll)

for i in range(1,4):
    action.move_by_offset(29,0).perform()

action.release()

sleep(2)
print(bro.page_source)
bro.quit()