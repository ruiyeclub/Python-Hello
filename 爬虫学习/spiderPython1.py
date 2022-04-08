# 爬虫下载

import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'
# urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
url_img = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_match%2F0%2F9689449571%2F0.jpg&refer=http%3A%2F%2Finews.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1643276199&t=910e45276ab024822dba4035eb12da1d'
urllib.request.urlretrieve(url_img, 'zrn.jpg')

# 下载视频...同理
