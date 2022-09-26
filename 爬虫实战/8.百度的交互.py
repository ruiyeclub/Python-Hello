# 使用selenium操作百度自动操作

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("../selenium/chromedriver.exe")
browser = webdriver.Chrome(service=s)
url = 'https://www.baidu.com'
browser.get(url)

# 获取文本框的对象
input = browser.find_element(by=By.ID, value='kw')

# 在文本框中输入周杰伦
input.send_keys('周杰伦')

# 获取百度一下的按钮
button = browser.find_element(by=By.ID, value='su')
# 点击按钮
button.click()

time.sleep(2)

# 滑倒底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页的按钮
next = browser.find_element(by=By.XPATH, value='//a[@class="n"]')
# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.back()

time.sleep(2)

# 回去
browser.forward()

time.sleep(2)

browser.quit()
