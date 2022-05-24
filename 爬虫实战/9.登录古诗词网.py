# 通过登录进入到主页面

'''
登录所需的参数
__VIEWSTATE: /pUic86mk/W8xe268J7T/mSECHzeE4FYgyh5KqtgHoYtNdMXYkAtm/YuiXrHKoo9f3w1vm2xqqaeJ0tguVe15TieJKDySwcfn16BYTm0YPLkqQUyqGxbB2aemAs=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://so.gushiwen.cn/user/collect.aspx
email: 15773329913
pwd: 561465465
code: ovtk
denglu: 登录

注意：前面两个参数是变量
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/pUic86mk/W8xe268J7T/mSECHzeE4FYgyh5KqtgHoYtNdMXYkAtm/YuiXrHKoo9f3w1vm2xqqaeJ0tguVe15TieJKDySwcfn16BYTm0YPLkqQUyqGxbB2aemAs=" />
<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="C93BE1AE" />
'''

import requests
from bs4 import BeautifulSoup
import urllib.request


# 该方法有问题，相当于请求了两次验证码接口，导致需要验证的验证码不是输入的验证码
def get_content(code_url):
    # 将图片下载到本地
    urllib.request.urlretrieve(url=code_url, filename='code.jpg')
    code_name = input('请输入你的验证码')

    data_post = {
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': view_state_generator,
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '15773329913',
        'pwd': 'action',
        'code': code_name,
        'denglu': '登录',
    }

    response_post = requests.post(url=url, headers=headers, data=data_post)
    return response_post


# requests里面有一个方法session() 通过session的返回值 就能使用请求变成一个对象
def get_content_by_session(code_url):
    session = requests.session()
    # 请求验证码url的session和后面请求接口的session是一个session
    response_code = session.get(code_url)
    content_code = response_code.content
    with open('code.jpg', 'wb')as fp:
        fp.write(content_code)
    code_name = input('请输入你的验证码')

    data_post = {
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': view_state_generator,
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '15773329913',
        'pwd': 'action',
        'code': code_name,
        'denglu': '登录',
    }

    response_post = session.post(url=url, headers=headers, data=data_post)
    return response_post


if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    # 获取页面的源码
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
    # 获取response内容
    response_post = get_content_by_session(code_url)

    content_post = response_post.text
    with open('gushiwen.html', 'w', encoding=' utf-8') as fp:
        fp.write(content_post)
