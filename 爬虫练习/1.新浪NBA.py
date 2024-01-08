'''
技术总结：
xpath/jsonpath/bs4的区别
xpath和bs4类似，处理html或xml，查找/替换等操作。
jsonpath，把（json格式的）字符串转换为json对象
'''

import urllib.request

from lxml import etree

# 练习内容：获取（https://nba.hupu.com/stats/players）中球星得分榜排名

url = 'https://nba.hupu.com/stats/players'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
etree = etree.HTML(content)

# 获取内容
name_list = etree.xpath("//tbody/tr/td[@class='left']/a/text()")
point_list = etree.xpath("//tbody/tr/td[@class='bg_b']/text()")
for i in range(len(name_list)):
    print(name_list[i] + ":" + point_list[i])
