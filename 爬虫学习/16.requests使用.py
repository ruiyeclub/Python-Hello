'''
安装：pip install requests
'''

import requests
import json


# response的属性以及类型 类型 ：models.Response
# r.text : 获取网站源码
# r.encoding ：访问或定制编码方式
# r.url ：获取请求的url
# r.content ：响应的字节类型
# r.status_code ：响应的状态码
# r.headers ：响应的头信息

def test_response():
    url = 'http://www.baidu.com'
    response = requests.get(url=url)
    # 设置响应的编码格式
    response.encoding = 'utf-8'
    # 以字符串的形式来返回了网页的源码
    print(response.text)


# 总结：
# 1.参数使用params传递
# 2.参数无需urlencode编码
# 3.不需要请求对象的定制
# 4.请求资源路径中的?可以加也可以不加

def test_get():
    url = 'https://www.baidu.com/s'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    data = {
        'wd': '长沙'
    }
    # url 请求资源路径
    # params 参数
    # kwargs 字典
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    print(content)


# 总结：
# 1.post请求不需要编解码
# 2.post请求的参数是data
# 3.不需要请求对象的定制

def test_post():
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    data = {
        'kw': 'eye'
    }
    response = requests.post(url=url, data=data, headers=headers)
    content = response.text
    json_str = json.loads(content)
    print(json_str)


def test_proxy():
    url = 'http://www.baidu.com/s?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    data = {
        'wd': 'ip'
    }
    # 代理
    proxy = {
        'http': '212.129.251.55:16816'
    }
    response = requests.get(url=url, params=data, headers=headers, proxies=proxy)
    content = response.text
    with open('daili.html', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    test_proxy()
