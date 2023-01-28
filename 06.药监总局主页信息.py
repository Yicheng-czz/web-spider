from urllib.request import urlopen

import requests
import json
from bs4 import BeautifulSoup

'''
date : 2021/7/20
author : Yicheng
'''

url = "http://scxk.nmpa.gov.cn:81/xk/"  # 药监总局地址

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# 该网站通过ajax请求动态加载数据
info_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
info_param = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
}
# 详情页中的信息也是动态加载出来的
# 主页用于获取id  列表信息
detail_urls = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
# 详情页地址     每个公司的详情
details_urls = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
response = requests.post(url=info_url, data=info_param, headers=header)
page_json = response.json()
AllData = []
# filename = "xk.json"
for url_id in page_json["list"]:
    print(url_id['ID'])
    param = {'id': url_id['ID']}

    response_detail = requests.post(url=details_urls, data=param, headers=header)
    page_response_detail = response_detail.json()
    AllData.append(page_response_detail)
    #print(page_response_detail)

with open("AllDate.json", 'w', encoding="utf-8") as fp:
    json.dump(AllData, fp=fp, ensure_ascii=False)
    # filename = "药监" + str(url_id['NUM_']) + ".json"
    # with open(filename, "w", encoding="utf-8") as fp:
    #     # fp.write(page_response_detail)
    #     json.dump(page_response_detail, fp, ensure_ascii=False)
    #     print(str(url_id['NUM_']) + " ok!")
# with open(filename, "w", encoding="utf-8") as fp:
#     json.dump(page_json, fp, ensure_ascii=False)
# print(page_json)
print(AllData)