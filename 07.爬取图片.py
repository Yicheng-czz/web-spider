import requests

'''
date : 2021/7/20
author : Yicheng
'''

url = 'https://pic.qiushibaike.com/system/pictures/12449/124490192/medium/XZ4B03YA8AM2ILC0.jpg'

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

response = requests.get(url=url, headers=header)
print(response.content)
with open("./qiutu.jpg",'wb') as fp:
    fp.write(response.content)


