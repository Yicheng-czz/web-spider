# 目的：在爬虫中使用异步实现高性能的数据爬取操作
from multiprocessing.dummy import Pool
import time

'''
date : 2021/7/22
author : Yicheng
'''

name_list = ['aa', 'bb', 'cc', 'dd']

time_start = time.time()


def get_name(name):
    print("正在下载:", name)
    time.sleep(2)
    print(name, "下载成功")


pool = Pool(4)

pool.map(get_name, name_list)

time_end = time.time()
print(time_end - time_start)
