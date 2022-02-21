# 请求对象的定制（request）
# quote方法 将内容变成Unicode编码格式

import urllib.parse
import urllib.request

# 将自己伪装成浏览器 User Agent用户代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

# url = 'https://www.baidu.com'
# 将输入的内容变成Unicode编码的格式
name = urllib.parse.quote('周杰伦')
# print(name) %E5%91%A8%E6%9D%B0%E4%BC%A6
url = 'https://www.baidu.com/s?wd=' + name
print(url)

# 本来直接传url, headers没有任何问题，但是里面参数很多找不到对应的参数
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
