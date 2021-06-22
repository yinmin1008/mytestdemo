
# 用print函数打印多个值
# print('a','b','c')

# 用print函数换行打印
# print('a\nbc')

# 导入模块的方式有哪些
import math
import random

from class02bukebian.demo01 import test01
from class02bukebian.demo01 import *

# 分别对49.698作如下打印
a = 49.698
    # 1）四舍五入，保留两位小数
print(round(a,2))

	# 2）向上入取整
print(math.ceil(a))

	# 3）向下舍取整
print(math.floor(a))

	# 4）计算8除以5返回整型
print(8//5)

	# 5）求4的2次幂
print(4**2)
	# 6）返回一个（1,100）随机整数
print(random.random())
print(random.randint(1,100))

# 依次对变量a,b,c赋值为1,2,3
a,b,c = 1,2,3
print(a)
print(b)
print(c)

# 截取某字符串中从2索引位置到最后的字符子串
a = 'sadsdgdfhygmj'
print(a[2:])

# 对字符串“testcode”做如下处理：
b = 'testcode'
    # 1）翻转字符串
print(b[::-1])

    # 2）首字母大写
print(b.capitalize())

    # 3）查找是否包含code子串，并返回索引值
print(b.find('code'))

    # 4）判断字符串的长度
print(len(b))

    # 5）从头部截取4个长度字符串
print(b[0:4])

    # 6）把code替换为123
print(b.replace('code','123'))

    # 7）把“testcode”字符串中的两个单词转换为列表中的元素，并打印处理
print(list(b))

# 讲小数转为整数
c = 2.33
print(int(c))

# 如何打印出字符串“test\ncode”
print(r'test\ncode')
print('test\\ncode')

# 按逗号分割列表当中的元素 list=[1,2,3,4,5,6]  输出1，2，3，4，5，6
list=[1,2,3,4,5,6]
s1 = ','.join(str(n) for n in list)
print(s1)

# 字符串"Hey, you - what are you doing here!?"
# 分割成'Hey', 'you', 'what', 'are', 'you', 'doing', 'here'
d = "Hey, you - what are you doing here!?"
print(d.split(' '))
# print(d.findall(r'[\w]+',str1))

