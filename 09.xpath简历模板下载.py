from lxml import etree
import requests
import os

'''
date : 2021/7/20
author : Yicheng
'''

# 从第一页开始爬取
url = "https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&issale=&classID=864&page=1"

# UA伪装
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

# 拼接url，以进行翻页操作
cut_url = url.split("page")[0]
print(cut_url)

# 模板列表页循环
for i in range(1,3):
    # 获取模板列表页
    result = requests.get(url=(cut_url+"page="+str(i)),headers=header).text
    # 实例化etree对象
    tree = etree.HTML(result)
    # 获取每个模板对应的详情页地址
    moban_list = tree.xpath("//div[@id='main']/div/div/a/@href")
    print(moban_list)

    # 循环进入每个模板的详情页
    for x in moban_list:
        # 拼接详情页地址
        detail_url = "https:"+x
        # 进入详情页，并获取详情页
        detail_page = requests.get(url=detail_url,headers=header).text
        # 实例化etree对象
        detail_page_tree = etree.HTML(detail_page)
        # 获取每个模板的的下载链接
        download_url = detail_page_tree.xpath('//ul[@class="clearfix"]/li[4]/a/@href')
        # print(download_url[0])
        # 获取下载内容的二进制
        download = requests.get(url=download_url[0],headers=header).content
        # 拼接文件名
        rar_name = download_url[0].split('/')[-1]
        # 将压缩文件的二进制写入
        with open("./简历模板/"+rar_name,'wb') as fp:
            fp.write(download)
        # for y in download_url:




