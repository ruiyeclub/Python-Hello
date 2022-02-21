# 查询KFC附近的店
import urllib.request

if __name__ == '__main__':
    start_index = int(input('请输入页码'))

    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    data = {
        'cname': '长沙',
        'pid': '',
        'pageIndex': int(start_index),
        'pageSize': 10
    }

    # post请求的参数 必须进行编码
    data = urllib.parse.urlencode(data).encode('utf-8')

    # 请求对象的定制
    request = urllib.request.Request(url=url, headers=headers, data=data)

    # 获取响应的数据
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    # 数据下载到本地
    with open('kfc' + str(start_index) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)
