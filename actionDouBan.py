# get请求
# 获取豆瓣电影的第一页的数据 并且保存起来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

# 1.请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 2.获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# print(json.loads(content))

# 3.数据下载到本地 (open方法默认使用的是gbk的编码)
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)

# 这种写法和上面的写法没什么区别 但是可以省去写关闭fp
with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
