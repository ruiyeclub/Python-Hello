# post请求

import json
import urllib.request

url = 'https://fanyi.baidu.com/sug'

# 将自己伪装成浏览器 User Agent用户代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# post请求的参数 必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求的参数 是不会拼接在url的后面的 而是需要放在请求对象定制的参数中
# post请求的参数 必须要进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

print(content)

# 将字符串转化成json类型
print(json.loads(content))

# python发送post请求分为表单类（x-www-form-urlencoded）和json（application/json）格式
import requests

new_url = "https://fanyi.baidu.com/sug"
new_data = {'kw': 'spider'}
new_res = requests.post(url=new_url, data=new_data)
print(json.loads(new_res.text))
