# -*-coding:utf8-*-

import requests
import json
import random
import pymysql
import sys
import datetime
import time
from imp import reload
from multiprocessing.dummy import Pool as ThreadPool

from bs4 import BeautifulSoup

url = "https://www.bilibili.com/v/popular/rank/all/"

# 发送GET请求获取网页内容
response = requests.get(url)

# 确保请求成功
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 进行数据提取和处理
    # 在这里可以使用BeautifulSoup的各种方法来定位和提取您所需的数据
    print(soup)

    # 示例：提取排行榜的视频标题
    video_titles = soup.select('.info .title')
    for title in video_titles:
        print(title.get_text())
else:
    print("请求失败，状态码：", response.status_code)

