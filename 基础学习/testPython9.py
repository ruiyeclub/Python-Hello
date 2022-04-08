# a:是append的缩写 直接在文件后面追加内容
# fp = open('test.txt', 'a')
# fp.write('hello world\n' * 5)

# 读数据 默认清空下read是一字节一字节的读 效率比较低
fp = open('test.txt', 'r')
content = fp.read()
# print(content)
# fp.close()

# 读数据 readlines是一行一行的读 *读取打印的是数组*
content_list = fp.readlines()
print(content_list)
