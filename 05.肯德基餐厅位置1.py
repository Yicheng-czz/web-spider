import requests
import json

'''
date : 2021/7/20
author : Yicheng
'''


def Kfc():
    keyword = input("请输入城市名称：")
    for i in range(1, 3):
        pms = {
            'cname': '',
            'pid': '',
            'keyword': keyword,
            'pageIndex': i,
            'pageSize': '10'
        }
        res = requests.post(url=url, data=pms, headers=headers)
        data = res.json()
        fileName = "KFC" + str(i) + ".json"
        with open(fileName, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False)


if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
    Kfc()
