# tuple元组使用的是()，且无法修改 数组使用的是[]且可以修改
# 定义只有一个数据的元组 需要在数据后面放有个“,”

a_tuple = (1, 232, 4, '1')
print(a_tuple[1])

# 切片是指对对象截取一部分内容进行操作，eg: 字符串、数组、元组都支持。

s = 'hello world'
# 遵循左闭右开区间 打印hell
print(s[0:4])

print(s[0:5:2])
