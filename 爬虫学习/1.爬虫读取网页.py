# 爬虫：1通过程序，根据url（taobao.com）进行爬取网页，获取有用的信息
#      2使用程序模拟浏览器，向服务器发起请求，获取响应信息

# 使用urllib来获取百度首页的源码
import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# 获取请求状态码
print(response.getcode())

# 获取请求状态信息
print(response.getheaders())

# 获取请求状态信息
print(response.geturl())

# 获取响应中的页面源码 read()方法返回的是字节形式的二进制数据
# 二进制 -> 字符串 解码 需要decode
# content = response.read().decode('utf-8')
content = response.readlines()
print(content)
