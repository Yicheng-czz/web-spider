import os

from lxml import etree
import requests

'''
date : 2021/7/20
author : Yicheng
'''

url = 'https://pic.netbian.com/4kmeinv/'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

result = requests.get(url=url, headers=header).content.decode("gbk")
# print(result)
tree = etree.HTML(result)

# 找到class=clearfix的div标签下的li 的img的地址
src_url_list = tree.xpath('//ul[@class="clearfix"]/li//img/@src')
print(src_url_list)

# 若该文件夹不存在，则创建该文件夹
if not os.path.exists("./meitu"):
    os.mkdir("./meitu")

# 遍历每个图片的地址
for i in src_url_list:
    # 拼接图片网址
    detail_url = 'https://pic.netbian.com'+i
    # 使用二进制显示图片源码
    detail = requests.get(url=detail_url,headers=header).content

    # 截取图片文件名称
    img_name = i.split("/")[-1]

    # 以二进制写入图片文件
    with open("./meitu/"+img_name,"wb") as fp:
        fp.write(detail)


