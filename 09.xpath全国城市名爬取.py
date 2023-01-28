from lxml import etree
import requests
import os

'''
date : 2021/7/20
author : Yicheng
'''

url = 'https://www.aqistudy.cn/historydata/'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

result = requests.get(url=url, headers=header).text

# print(result)
tree = etree.HTML(result)

hot_city_list = tree.xpath('//div[@class="hot"]//ul[@class="unstyled"]/li/a/text()')
print(hot_city_list)
all_city_list = tree.xpath('//div[@class="all"]//li/a/text()')
print(all_city_list)


if not os.path.exists("./cities.txt"):
    os.mkdir("./cities.txt")

with open("./cities.txt", "a+",encoding="utf-8") as fp:
    fp.write("热门城市：\n")
for i in hot_city_list:
    with open("./cities.txt","a+",encoding="utf-8") as fp:
        fp.write(i+"\n")

with open("./cities.txt", "a+",encoding="utf-8") as fp:
    fp.write("全部城市：\n")
for i in all_city_list:
    with open("./cities.txt","a+",encoding="utf-8") as fp:
        fp.write(i+"\n")


