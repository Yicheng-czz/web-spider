import requests
import re

# 需求：爬取糗事百科糗图模块下的所有糗图

'''
date : 2021/7/20
author : Yicheng
'''

url = 'https://www.qiushibaike.com/imgrank/'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

# 翻页
for i in range(1, 14):
    # 更新 翻页的url地址
    url = url + "page/" + str(i) + "/"
    # 获取文本
    response = requests.get(url=url, headers=header).text

    # 正则表达式
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    # 找到所有对应的图片网址
    img_src_list = re.findall(ex, response, re.S)
    # 打印每页的图片地址列表
    print(img_src_list)

    # 遍历每页中的图片
    for i in img_src_list:
        # 请求每一张图片的二进制资源
        img_detail = requests.get("https:" + i, headers=header).content
        # 图片名称通过地址.split最后一截的字符串.jpg生成
        img_name = i.split("/")[-1]
        # 持久化保存
        with open("./糗图资源/" + img_name, "wb") as fp:
            fp.write(img_detail)
