# 爬虫异常
# HTTPError类是URLError类的子类
# 通过urllib发送请求的时候，有可能会发送失败，这个时候如果想让你的代码更加的健壮，
# 可以通过try-except进行捕获异常，异常有两类，URLError/HTTPError。

import urllib.request
from urllib.error import HTTPError, URLError

# url = 'https://www.cnblogs.com/gaffey/p/159233021.html'
url = 'https://www.hdiahisofd.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except HTTPError:
    print('这是HTTPError')
except URLError:
    print('这是URLError')
