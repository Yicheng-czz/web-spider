from bs4 import BeautifulSoup as bs
import lxml
import requests
import re

'''
date : 2021/7/20
author : Yicheng
'''


# url = "https://www.qiushibaike.com/"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
# result = requests.get(url=url, headers=headers).text
# print(result)
url = 'D:\VS code project\shopping品优购项目\index.html'
# <span class="recmd-name">威趣贝</span>
f = open(url,'r',encoding='utf-8')
bs1 = bs(f, 'lxml')
span_all = bs1.find_all('div', class_='dd')
print(span_all[0])

for i in range(0,15):
    # 用select获取文本内容
    print(bs1.select(".dd > ul > li > a")[i].get_text())
    # 获取a标签中的href属性值
    print(bs1.select(".dd > ul > li > a")[i]['href'])
