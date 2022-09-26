'''
Selenium：可以模拟浏览器功能，自动执行网页中的js代码，实现动态加载
1.selenium是一个用于web应用程序测试的工具
2.selenium测试直接运行在浏览器中，就像真正的用户在操作一样
3.支持通过各种driver（火狐/谷歌...），驱动真实浏览器完成测试
4.selenium也是支持无页面浏览器操作的

3.如何安装selenium？
（1）操作谷歌浏览器驱动下载地址 http://chromedriver.storage.googleapis.com/index.html
（2）谷歌驱动和谷歌浏览器版本之间的映射表 http://blog.csdn.net/huilan_same/article/details/51896672
（3）查看谷歌浏览器版本 谷歌浏览器右上角‐‐>帮助‐‐>关于
（4）pip install selenium
'''

# 1.导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 2.创建浏览器操作对象
s = Service("../selenium/chromedriver.exe")

browser = webdriver.Chrome(service=s)

# 3.访问网站
url = 'https://www.baidu.com'

browser.get(url)

# page_source获取网页源码
# content = browser.page_source
# print(content)

# 元素定位

# 根据id查找对象 **
button = browser.find_element(by=By.ID, value='su')
print(button)

# 根据标签属性的属性值来获取对象
button1 = browser.find_element(by=By.NAME, value='wd')
print(button1)

# 根据标签的名字获取对象
button2 = browser.find_element(by=By.TAG_NAME, value='input')
print(button2)

# 根据xpath查找对象 **
button3 = browser.find_element(by=By.XPATH, value='//input[@id="su"]')
print(button3)

# 使用bs4的语法来获取对象 **
button4 = browser.find_element(by=By.CSS_SELECTOR, value='#su')
print(button4)

# 根据a标签的内容查找
button5 = browser.find_element(by=By.LINK_TEXT, value='新闻')
print(button5)

# 元素信息

# 获取标签的属性
print(button.get_attribute('class'))
# 获取标签的名字
print(button.tag_name)
# 获取元素文本
print(button5.text)

browser.quit()
