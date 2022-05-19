'''
1.请求对象的定制 request
2.模拟浏览器访问服务器，返回 response
3.获取网页源码 content
4.下载 write
'''

# 需求下载前十页的图片
# https://sc.chinaz.com/tupian/huangsetupian.html
# https://sc.chinaz.com/tupian/huangsetupian_2.html

import urllib.request
from lxml import etree


def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/huangsetupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/huangsetupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    # 下载图片
    tree = etree.HTML(content)
    name_list = tree.xpath("//div[@id='container']//a/img/@alt")
    # 一般涉及到图片的网站都会用到懒加载（本来是src2 加载完毕变成src）
    img_list = tree.xpath("//div[@id='container']//a/img/@src2")

    for i in range(len(name_list)):
        name = name_list[i]
        src = img_list[i]
        urllib.request.urlretrieve(url='https:' + src, filename='./img/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载内容
        down_load(content)
