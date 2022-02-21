# 文件
print('')

'''
open函数可以创建文件，或者打开一个文件。不可以创建文件夹
w：可写
r：可读
'''
# open('test.txt', 'w')

fp = open('test.txt', 'w')
fp.write('hhh222h')

# 写完文件需要关闭 关闭之后内存更小
fp.close()

fp = open('test.txt', 'w')
fp.write('hello world\n' * 5)
fp.close()
