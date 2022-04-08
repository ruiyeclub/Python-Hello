# 代理常用功能：1.突破自身IP访问限制，访问国外站点 2.访问一些单位或团体内部资源
# 3.提高访问速度 4.隐藏真实IP

import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
proxies = {
    '27.192.202.11': '9000'
}

# handler build_opener open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应信息
content = response.read().decode('utf-8')

# 保存
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
