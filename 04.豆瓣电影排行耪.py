import requests
import json

'''
date : 2021/7/20
author : Yicheng
'''

url = "https://movie.douban.com/j/chart/top_list"

param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': "0",
    'limit': "20"
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
i = 1


def getMovie(url, param, i):
    response = requests.get(url=url, params=param, headers=header)
    fileName = "Movie" + str(i) + ".json"
    with open(fileName, "w", encoding="utf-8") as fp:
        json.dump(response.json(), fp, ensure_ascii=False) # 因为有汉字，所以不能用ASCII编码

    start_i = int(param['start']) + 20
    limit_i = int(param['limit']) + 20
    param['start'] = str(start_i)
    param['limit'] = str(limit_i)
    print(param)
    i += 1

    getMovie(url, param, i)


getMovie(url, param, i)
# for item in response.json():
#     print(item['title'],item['regions'],item['types'],item['cover_url'])
# start += 20
# limit += 20
# param['start'] = str(start)
# param['limit'] = str(limit)
# getMovie(url,param,start,limit)
