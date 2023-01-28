from selenium import webdriver
from lxml import etree

chro = webdriver.Chrome(executable_path='chromedriver.exe')

'''
date : 2021/7/22
author : Yicheng
'''

# 打开页面
chro.get('http://scxk.nmpa.gov.cn:81/xk/')

# 获取页面源码
page_text = chro.page_source
# 实例化药监总局的etree对象
NMPA_tree = etree.HTML(page_text)

# 解析，获取公司名称
name_list = NMPA_tree.xpath('//ul[@class="hzblist"]/li/dl/@title')

# 打印公司列表名
print(name_list)

# 关闭网页
chro.quit()
