from selenium import webdriver
# 实现无头浏览器
from selenium.webdriver.chrome.options import Options
# 规避服务器端的检测
from selenium.webdriver import ChromeOptions

'''
date : 2021/7/22
author : Yicheng
'''

chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')

# 仿检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_option,options=option)

bro.get("https://www.baidu.com")

print(bro.page_source)

bro.quit()

