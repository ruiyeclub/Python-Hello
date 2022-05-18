# 获取百度页面源码中的百度一下四个字

'''
1.获取网页的源码
2.解析 解析的服务器响应的文件 etree.HTML
3.打印
'''

import urllib.request
from lxml import etree

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)

# 获取网页的源码
content = response.read().decode('utf-8')

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据 xpath返回的是列表类型的数据
result = tree.xpath('//input[@id="su"]/@value')

print(result)

