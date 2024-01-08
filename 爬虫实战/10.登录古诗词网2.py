'''
登录古诗词网升级版：
不需要手动输入验证码，使用第三方python库ddddocr自动识别

r:    以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
rb: 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+: 打开一个文件用于读写。文件指针将会放在文件的开头。
rb+:以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w:    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb:    以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+:    打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+:以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a:    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab:    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+:    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+:以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''

import ddddocr
import requests
from bs4 import BeautifulSoup

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

# 获取页面源码
response = requests.get(url=url, headers=headers)
content = response.text

# 解析页面源码
soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
view_state = soup.select('#__VIEWSTATE')[0].get('value')

# 获取__VIEWSTATEGENERATOR
view_state_generator = soup.select('#__VIEWSTATEGENERATOR')[0].get('value')

# 获取验证码
code = soup.select('#imgCode')[0].get('src')
code_url = 'https://so.gushiwen.cn' + code

# 使用session进行一次请求
session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content

# 使用ddddocr识别图片二维码
ocr = ddddocr.DdddOcr()
# 参数是bytes二进制
code_name = ocr.classification(content_code)

data_post = {
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '15773329913',
    'pwd': '185048761',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
