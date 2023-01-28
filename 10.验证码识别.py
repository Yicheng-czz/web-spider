import PIL.ImageQt
import pytesseract
from PIL import Image
import requests
from lxml import etree
# 外接API
from python爬虫实战 import chaojiying

'''
date : 2021/7/22
author : Yicheng
'''

# im = Image.open("./2.png")
# # im = im.convert('RGB')
# print(pytesseract.image_to_string(im,lang='chi_sim'))

login_url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

login_page = requests.get(url=login_url, headers=headers).text

login_page_tree = etree.HTML(login_page)

QR_code = login_page_tree.xpath('//div[@class="mainreg2"]/img[@id="imgCode"]/@src')

QR_code_url = login_url.split("/user")[0] + QR_code[0]

download_QR_code = requests.get(url=QR_code_url, headers=headers).content

with open("./QR_code.jpg", 'wb') as fp:
    fp.write(download_QR_code)

chaojiying = chaojiying.Chaojiying_Client('18267841597', 'QYCQyc1826784', '919257')
im = open('./QR_code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
print(chaojiying.PostPic(im, 1902))






