#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：MySpider 
@File    ：spider.py
@IDE     ：PyCharm 
@Author  ：离开流沙河的坚定大土豆
@Date    ：2024/4/7 13:07 
'''

import requests

def test():
    url = 'https://search.damai.cn/searchajax.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Cookie': 'cna=kXsjG6zEp0ICAd67lEXZsuHn; t=95c3aebb5de88b3ba303e2129d62bbe6; cookie2=106b37abb823a04b516de4f3b8329ee7; _tb_token_=f753afee7b845; xlly_s=1; _samesite_flag_=true; _hvn_login=18; munb=2214441568768; csg=741367b3; damai.cn_nickName=%E9%BA%A6%E5%AD%9037cVY; damai.cn_user=9+2lpmjNeo7V/YYxX8T2utQ+Jq4Eqq6W5VB3Cfnd3zKEgoZeXMtzK7Bu4OxYqRSrGxb2+Rjuqig=; damai.cn_user_new=9%2B2lpmjNeo7V%2FYYxX8T2utQ%2BJq4Eqq6W5VB3Cfnd3zKEgoZeXMtzK7Bu4OxYqRSrGxb2%2BRjuqig%3D; h5token=dd0ce5a4cd1e407fbd539b8ab6f16aee_1_1; damai_cn_user=9%2B2lpmjNeo7V%2FYYxX8T2utQ%2BJq4Eqq6W5VB3Cfnd3zKEgoZeXMtzK7Bu4OxYqRSrGxb2%2BRjuqig%3D; loginkey=dd0ce5a4cd1e407fbd539b8ab6f16aee_1_1; user_id=201544377; mtop_partitioned_detect=1; _m_h5_tk=f7b178ce4b2b24e143c8cb81e165704b_1712474177002; _m_h5_tk_enc=4703c717c6cdeb0a83ceeecf642d6306; destCity=%u6210%u90FD; XSRF-TOKEN=9dce8aef-7c7d-40b1-ba7b-8d14bf5268e6; isg=BCYmiTxJfKNDLCgHaQpm8sXUd5yoB2rBxIN24hDPEsklk8ateJe60Qxg648fD2LZ; tfstk=faGqTz48lIdVCsDg4uNaLgD2tSFY1WKB7fZ_SV0gloq0cEFaIcm0If9xl5Ra4ce_moTY_RmimRm_fq_xeDghGj9Y11PY65xBABOIlqFTs3bCSSqxr4Ug0fbBqq3Y6aQ5jpMokOya2g8ascVuZyz4ss20oUru-uf0Ss4GqUzTqlVgn-4lry4OIi2cnbhrsj5z0-xfwkVg_6g33k02p1fZa6w4xqqPsdczuhqnou5GsoEYSj0rln5KPShIYyiXZsoES2HgUfSkYlhrrjDiyi-gyAmbZoNHnaPjMqD3IXxOIDPqbJc0UNfnkqq8azcH59ESaoiig8YCTRNoOJVmFLKbCSzEjjnV71mnP2GYef-FqlHbJ74Z6eXabRjznGUl1chtSZWanzUzAU8lHoQGoIPCndBOB8Y8zkTe8OBTnz4zAU85BOeo8zrBlff..',
        'Referer': 'https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.592323e14H35am&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=%E6%88%90%E9%83%BD',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Xsrf-Token': '9dce8aef-7c7d-40b1-ba7b-8d14bf5268e6'
    }
    params = {
        'cty': '成都',
        'ctl': '演唱会',
        'sctl': None,
        'tsg': 0,
        'st': None,
        'et': None,
        'order': 1,
        'pageSize': 30,
        'currPage': 1,
        'tn': None
    }
    result = requests.get(url=url, headers=headers, params=params).json()
    print(result['pageData']['resultData'])


if __name__ == "__main__":
    test()
