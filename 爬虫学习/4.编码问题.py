# urlencode应用场景：多个参数的时候，进行编码
# https://www.baidu.com/s?wd=周杰伦&sex=男

import urllib.parse
import urllib.request

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
base_url = 'https://www.baidu.com/s?'
url = base_url + new_data

# 将自己伪装成浏览器 User Agent用户代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read().decode('utf-8')
print(content)
