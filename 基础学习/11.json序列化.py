# 序列化问题 讲内存中的数据转化成字节序列 可保存到文件中 对象->字节序列=序列化
# 反序列化 将字节序列恢复到内存中

# 默认情况下，对象是无法写入到文件里面的，需要将它序列化。
# 使用到JSON这个库 序列化的两种操作 dumps和dump

import json

a_list = ['cr', 18]

fp = open('test.txt', 'w')
# fp.write(json.dumps(a_list))
# fp.close()

# dump：将对象转化成json字符串的同时，指点文件，并将文件存储到里面去
json.dump(a_list, fp)
fp.close()

fp1 = open('test.txt', 'r')
result = json.load(fp1)
print(result)
