import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

# 开始bs4
soup = BeautifulSoup(content, 'lxml')

# xpath：//ul[@class='grid padded-3 product']//strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')

for name in name_list:
    print(name.get_text())