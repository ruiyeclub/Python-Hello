import schedule
import time
import urllib.request
import json
import redis
from datetime import datetime
import re

# 交易
pattern = "[거래]"

# 请求地址
url = 'https://api-manager.upbit.com/api/v1/notices?page=1&per_page=5&thread_name=general'

# 请求头
headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'cna=UkO6F8VULRwCAXTqq7dbS5A8; miid=949542021157939863; '
              'sgcookie=E100F01JK9XMmyoZRigjfmZKExNdRHQqPf4v9NIWIC1nnpnxyNgROLshAf0gz7lGnkKvwCnu1umyfirMSAWtubqc4g%3D'
              '%3D; tracknick=action_li; _cc_=UIHiLt3xSw%3D%3D; '
              'enc=dA18hg7jG1xapfVGPHoQCAkPQ4as1%2FEUqsG4M6AcAjHFFUM54HWpBv4AAm0MbQgqO%2BiZ5qkUeLIxljrHkOW%2BtQ%3D%3D'
              '; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _m_h5_tk=3ca69de1b9ad7dce614840fcd015dcdb_1629776735568; '
              '_m_h5_tk_enc=ab56df54999d1d2cac2f82753ae29f82; t=874e6ce33295bf6b95cfcfaff0af0db6; xlly_s=1; '
              'cookie2=13acd8f4dafac4f7bd2177d6710d60fe; v=0; _tb_token_=e65ebbe536158; '
              'tfstk=cGhRB7mNpnxkDmUx7YpDAMNM2gTGZbWLxUZN9U4ulewe025didli6j5AFPI8MEC..; '
              'l=eBrgmF1cOsMXqSxaBO5aFurza77tzIRb8sPzaNbMiInca6OdtFt_rNCK2Ns9SdtjgtfFBetPVKlOcRCEF3apbgiMW_N-1NKDSxJ6'
              '-; isg=BBoas2yXLzHdGp3pCh7XVmpja8A8S54lyLj1RySTHq14l7vRDNufNAjpZ2MLRxa9',
    'referer': 'https://upbit.com/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# 创建Redis连接对象
r = redis.Redis(host='localhost', port=6379, password='')


# 定时任务逻辑
def do_job():
    print("----------------开始定时任务", datetime.now())
    # 开始请求
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # 转化成json数据
    json_object = json.loads(content)
    if json_object["success"]:
        list_object = json_object["data"]["list"]
        for post in list_object:
            is_new = do_sql(post)
            if is_new is True:
                print("获取最新文章：", post["title"])
                # 处理发送消息的逻辑
                do_send(post)


def do_send(post):
    symbol = do_check(post["title"])
    if not symbol:
        # 返回false 不处理
        return
    # todo 处理发送消息逻辑


def do_check(string):
    if pattern in string:
        # 获取（）中的内容
        match = re.search(r'\((\S+?)\)', string)
        if match:
            symbol = match.group(1)
            # 判断返回的字符串必须是字母
            if re.match(r'^[A-Za-z]+$', symbol) is not None:
                return symbol
    return False


# 处理数据库逻辑
def do_sql(post):
    # 获取键值对
    key = "spider:articleId:" + str(post["id"])
    value = r.get(key)
    if value is None:

        r.set(key, post["title"])
        return True
    else:
        return False


# 每隔5分钟运行一次job函数
schedule.every(2).seconds.do(do_job)

while True:
    try:
        schedule.run_pending()  # 运行所有可以运行的任务
    except Exception as e:
        time.sleep(2)
        print(e)
