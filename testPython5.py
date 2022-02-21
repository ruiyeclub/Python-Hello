# 列表高级

a_list = ['a', 'b']
a_list.append('c')
print(a_list)

a_list.insert(0, 'o')
print(a_list)

b_list = ['d']
a_list.extend(b_list)
print(a_list)

# 列表的修改
a_list[0] = '我是第一'
print(a_list)

# 裂开的删除
'''
del：根据下标删除
pop：删除最后一个 *也可以根据下标删哦！！！
remove：根据内容删除
'''

del a_list[0]
print(a_list)

a_list.pop(1)
print(a_list)

a_list.remove('d')
print(a_list)
