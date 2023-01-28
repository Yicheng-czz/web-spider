import requests
from lxml import etree

'''
date : 2021/7/22
author : Yicheng
'''

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

# 在proxies参数中添加ip
page_text = requests.get(url=url,headers=headers,proxies={"https":'代理IP'}).text

with open("ip.html","w",encoding='utf-8') as fp:
    fp.write(page_text)

# page_text_tree = etree.HTML('./ip.html')
# ip = page_text_tree.xpath('//div[@class=ip-container_3hE06]/span/text()')
# print(ip)

