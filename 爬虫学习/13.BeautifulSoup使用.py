'''
1.beautifulsoup简称：bs4
2.什么是beautifulsoup，和lxml一样，是一个html的解析器，主要功能也是解析和提取数据
3.优缺点？ 缺点：效率没有lxml高 优点：接口设计人性化，使用方便
安装：pip install bs4
'''

from bs4 import BeautifulSoup

# 通过解析本地文件 来将bs4的基础语法进行讲解
# 默认打开的文件的编码格式是gbk 所以在打开文件的时候需要指定编码
soup = BeautifulSoup(open('13.BeautifulSoup使用.html', encoding='utf-8'), 'lxml')

# 根据标签名查找节点
# 找到的是第一个符合条件的数据（尚硅谷）
# print(soup.a.text)
# 获取标签的属性和属性值（获取a标签内的属性值{'href': '', 'id': '', 'class': ['a1']}）
# print(soup.a.attrs)

# bs4的一些函数
# （1）find
# 返回的是第一个符合条件的数据（尚硅谷）
# print(soup.find('a').text)

# 根据title的值来找到对应的标签对象（百度）
# print(soup.find('a', title="a2").text)

# 根据class的值来找到对应的标签对象 注意的是class需要添加下划线（尚硅谷）
# print(soup.find('a', class_="a1").text)


# （2）find_all返回的是一个列表 并且返回了所有的a标签（[<a class="a1" href="" id="">尚硅谷</a>, <a href="" title="a2">百度</a>]）
# print(soup.find_all('a'))

# 如果想获取的是多个标签的数据 那么需要在find_all的参数中添加的是列表的数据（[<a class="a1" href="" id="">尚硅谷</a>, <span>嘿嘿嘿</span>, <a href="" title="a2">百度</a>, <span>哈哈哈</span>]）
# print(soup.find_all(['a', 'span']))

# limit的作用是查找前几个数据（[<li id="l1">张三</li>, <li id="l2">李四</li>]）
# print(soup.find_all('li', limit=2))


# （3）select（推荐）
# select方法返回的是一个列表 并且会返回多个数据（[<a class="a1" href="" id="">尚硅谷</a>, <a href="" title="a2">百度</a>]）
# print(soup.select('a'))

# 可以通过.代表class 我们把这种操作叫做类选择器（[<a class="a1" href="" id="">尚硅谷</a>]）
# print(soup.select('.a1'))
# #代表id（[<li id="l1">张三</li>]）
# print(soup.select('#l1'))


# 属性选择器---通过属性来寻找对应的标签
# 查找到li标签中有id的标签（[<li id="l1">张三</li>, <li id="l2">李四</li>]）
# print(soup.select('li[id]'))

# 查找到li标签中id为l2的标签（[<li id="l2">李四</li>]）
# print(soup.select('li[id="l2"]'))


# 层级选择器
# 后代选择器
# 找到的是div下面的li（[<li id="l1">张三</li>, <li id="l2">李四</li>, <li>王五</li>]）
# print(soup.select('div li'))

# 子代选择器
# 某标签的第一级子标签
# 注意：很多的计算机编程语言中 如果不加空格不会输出内容 但是在bs4中 不会报错 会显示内容（[<li id="l1">张三</li>, <li id="l2">李四</li>, <li>王五</li>]）
# print(soup.select('div > ul > li'))


# 找到a标签和li标签的所有的对象（[<li id="l1">张三</li>, <li id="l2">李四</li>, <li>王五</li>, <a class="a1" href="" id="">尚硅谷</a>, <a href="" title="a2">百度</a>]）
# print(soup.select('a,li'))

# 节点信息
# 获取节点内容 需要确定是否是单个对象 非则会报错
obj = soup.select('#d1')[0]
# 如果标签对象中 只有内容 那么string和get_text()都可以使用
# 如果标签对象中 除了内容还有标签 那么string就获取不到数据 而get_text()是可以获取数据
# 我们一般情况下  推荐使用get_text()（哈哈哈）
# print(obj.string)
# print(obj.get_text())

# 节点的属性
obj = soup.select('#p1')[0]
# name是标签的名字（p）
# print(obj.name)
# 将属性值左右一个字典返回（{'id': 'p1', 'class': ['p1']}）
# print(obj.attrs)

# 获取节点的属性 （['p1']）
obj = soup.select('#p1')[0]
# print(obj.attrs.get('class'))
# print(obj.get('class'))
# print(obj['class'])

# <a href="" title="a2" id="f1" value="value京东">京东</a>
print(soup.select('#f1')[0].get('value'))
