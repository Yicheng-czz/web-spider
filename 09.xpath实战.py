from lxml import etree
import requests

'''
date : 2021/7/20
author : Yicheng
'''

url = 'https://szkunshan.58.com/ershoufang/p1/?PGTID=0d100000-0001-0129-7bdd-15ccb8e718f5&ClickID=1'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

result = requests.get(url=url, headers=header).text
print(result)
tree = etree.HTML(result)

titles = tree.xpath('//div[@class="property-content-title"]/h3/text()')
with open("./describtion_of_house.txt",'a+',encoding='utf-8') as fp:
    for i in titles:
        fp.write(i+'\n')
print("------------------------------")
print(titles)

