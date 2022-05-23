'''
chrome-handless模式，google针对chrome浏览器59版新增加的额一个模式，
可以让你不打开ui界面的情况下使用chrome浏览器，运行效果与chrome保持一致。
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def get_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 创建浏览器操作对象
    s = Service("../selenium/chromedriver.exe")

    # path是你自己的chrome浏览器的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(options=chrome_options, service=s)
    return browser


if __name__ == '__main__':
    browser = get_browser()
    url = 'https://www.baidu.com'
    browser.get(url)

    content = browser.page_source
    print(content)
