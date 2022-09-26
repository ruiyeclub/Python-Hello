# - 获取长度:len                     len函数可以获取字符串的长度。
# - 查找内容:find                    查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次出现的开始位置索引值，如果不存在，则返回-1.
# - 判断:startswith,endswith        判断字符串是不是以谁谁谁开头/结尾
# - 计算出现次数:count                返回 str在start和end之间 在 mystr里面出现的次数
# - 替换内容:replace                 替换字符串中指定的内容，如果指定次数count，则替换不会超过count次。
# - 切割字符串:split                  通过参数的内容切割字符串
# - 修改大小写:upper,lower           将字符串中的大小写互换
# -  空格处理:strip                   去空格
# - 字符串拼接:join                   字符串拼接

# len  length的缩写  长度
s = '12'
print(len(s))

s1 = 'china'
print(s1.find('a'))

s2 = 'china'
print(s2.startswith('h'))
print(s2.endswith('n'))

s3 = 'aaabb'
print(s3.count('b'))

s4 = 'cccdd'
print(s4.replace('c', 'd'))

s5 = '1#2#3#4'
print(s5.split('#'))

s6 = 'china'
print(s6.upper())

s7 = 'CHINA'
print(s7.lower())

s8 = '   a   '
print(len(s8))

print(len(s8.strip()))

s9 = 'a'
print(s9.join('hello'))
