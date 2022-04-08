# actionDouBan的进阶版
import urllib.request

if __name__ == '__main__':

    start_page = int(input('请输入起始页'))
    end_page = int(input('请输入结束页'))

    for page in range(start_page, end_page + 1):
        start = (page - 1) * 20
        url = 'https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=' + str(
            start) + '&limit=20'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }

        # 1.请求对象的定制
        request = urllib.request.Request(url=url, headers=headers)

        # 2.获取响应的数据
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')

        # 3.数据下载到本地
        with open('douban' + str(page) + '.json', 'w', encoding='utf-8') as fp:
            fp.write(content)
