from lxml import etree
# xpath解析：
# 1.本地文件        etree.parse
# 2.服务器响应的数据 etree.HTML()

'''
xpath基本语法
1.路径查询：//：查询所有子孙节点，不考虑层级关系
           /：直接查找子节点
2.谓词查找：//div[@id] or //div[@id="maincontent"]
3.属性查询：//@class
4.模糊查询：//div[contains(@id, "he")] or //div[starts-with(@id, "he")]
5.内容查询：//div/h1/text()
6.逻辑运算：//div[@id="head" and @class="s_down"]
           //title | //price
'''

# xpath解析本地文件
tree = etree.parse('11.xpath基本使用.html')

# 查找ul下面的li
# li_list = tree.xpath('//body/ul/li')

# 查询所有有id属性的li标签
# li_list = tree.xpath('//ul/li[@id]/text()')

# 查询id为l1的li标签
# li_list = tree.xpath("//li[@id='l1']/text()")

# 查找到id为l1的li标签的class属性值
# li_list = tree.xpath('//li[@id="l1"]/@class')

# 查找到id中包含1的li标签
li_list = tree.xpath('//li[contains(@id, "1")]/text()')

print(li_list)