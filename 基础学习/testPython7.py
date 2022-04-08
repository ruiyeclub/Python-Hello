# 字典高级 查询

persion = {'name': 'zhansan', 'age': 12}
print(persion['name'])
print(persion.get('age'))

# 会报错
# print(persion['sex'])
# 不会报错 打印none
print(persion.get('sex'))

# 字典高级 修改
persion['age'] = 18
print(persion)

# 字典高级 添加（和修改一样的操作）
persion['sex'] = True
print(persion)

# 字典高级 删除

'''
del: 删除指点元素
clear() 清空整个对象 保留字典对象
'''

del persion['sex']
print(persion)
# persion.clear()
# print(persion)

# 字典高级 遍历
# 遍历key
for key in persion.keys():
    print(key)

# 遍历value
for value in persion.values():
    print(value)

# 遍历字典key和value
for key, value in persion.items():
    print(key, value)

# 遍历字典key和value
for key, value in persion.keys(), persion.values():
    print(key, value)

# 遍历字典的元素
for item in persion.items():
    print(item)
    print(type(item))
