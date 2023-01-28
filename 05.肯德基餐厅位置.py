import requests
import json

'''
date : 2021/7/20
author : Yicheng
'''

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
location = input("输入城市：")
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
i = 0
data = {
    'cname': '',
    'pid': '',
    'keyword': location,
    'pageIndex': i,
    'pageSize': '10'
}
response = requests.post(url=post_url, data=data, headers=header)
page_text = response.json()
filename = location + ".txt"
with open(filename, "w", encoding="utf-8") as fp:
    # fp.write(page_text)
    json.dump(page_text, fp, ensure_ascii=False)

print("成功")
