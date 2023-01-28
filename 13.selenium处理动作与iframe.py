from selenium import webdriver
# from lxml import etree
from time import sleep
# 导入动作链模块，常用于验证码滑动
from selenium.webdriver import ActionChains

'''
date : 2021/7/22
author : Yicheng
'''

bro = webdriver.Chrome("chromedriver.exe")

bro.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

# 切换作用域至内嵌网页，若定位标签存在于iframe标签中，需要用switch_to
bro.switch_to.frame('iframeResult')

# 获取拖动元素
div = bro.find_element_by_id('draggable')
# print(div)

# 实例化 将浏览器对象当作参数传入
action = ActionChains(bro)
# 点击并长按div对象
action.click_and_hold(div)

for i in range(5):
    # perform() 立即执行
    # move_by_offset(x,y) 移动
    action.move_by_offset(17,0).perform()
    sleep(0.5)

# 释放
action.release()

sleep(2)

bro.quit()