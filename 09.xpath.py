from lxml import etree
import requests

'''
date : 2021/7/20
author : Yicheng
'''

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
url2 = 'file:///D:/%E5%BE%AE%E4%BF%A1%E7%BC%93%E5%AD%98/WeChat%20Files/wxid_yks43qsgnfx411/FileStorage/File/2021-07/company.html'
header = {
    'User-Agent': "'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'"}

# 实例化etree对象，且将解析源码加载到对象
#result = requests.get(url=url, headers=header).content.decode('utf-8')

tree = etree.parse(url2,etree.HTMLParser())
t = tree.xpath('/html/body//div[@class="zw3"]/text()') # / 从根节点开始定位;  // 多个层级
for i in t:
    print(i)
