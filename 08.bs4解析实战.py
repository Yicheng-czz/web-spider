# https://www.shicimingju.com/book/sanguoyanyi.html
# 需求：爬取三国演义的章节名称
import requests
from bs4 import BeautifulSoup

'''
date : 2021/7/20
author : Yicheng
'''


url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

# .content.decode('utf-8') 解决乱码问题
result = requests.get(url=url,headers=header).content.decode('utf-8')

soup = BeautifulSoup(result,'lxml')

for i in range(0,120):
    # 爬取目录
    chapters = soup.select('.book-mulu > ul > li > a')[i].get_text()
    print(chapters)

    # 获取目录链接
    text_url = soup.select('.book-mulu > ul > li > a')[i]['href']
    print(url)

    # 爬取每一章对应的详情页
    result = requests.get(url="https://www.shicimingju.com/"+text_url,headers=header).content.decode('utf-8')
    # print(result)
    text_soup = BeautifulSoup(result,'lxml')
    text = text_soup.select('.chapter_content')[0].get_text()
    print(text)

    with open("./三国演义.html","a+",encoding='utf-8') as fp:
        fp.write(chapters)
        fp.write(text)

# print(chapters)



