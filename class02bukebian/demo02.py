# 数据类型
# 可变数据类型：字典dict，列表list，集合set
# 不可变数据类型：数字number，字符串string，元组tuple

# 数字number:   整数 int  小数 float  bool:  True 1  False 0
# 打印数据类型  type()


# a = 1
# print(a,type(a))
# b = 1.5
# print(b,type(b))
# c = True
# print(c,type(c))

# 数字可以进行运算  运算符  + — * /除 小数除  %取余数  **乘方  //除 整数除
a = 10
b = 20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)

# 比较符   == 相等  !=不想等  <= 小于等于   >= 大于等于  < 小于   > 大于   结果只有Ture和False    =为赋值   ==为相等
# print(1==1)
# print(1!=1)
# print(1<=1)
# print(1>=1)
# print(1<1)
# print(1>1)

# 赋值运算符  =等于  +=加等于   -= 减等于  *= 乘等于    /=除等于
a = 3
b = 6
# a +=b
# print(a)
# # a +=b 就等于  a = a+b
# # a -=b
# print(a)
# # a *=b
# print(a)
# a /=b
# print(a)

# 数据类型进行转换
a1 = 1.5
b1 = 2
# print(a1,type(a1))
# print(b1,type(b1))
# # 浮点数转换成整数
# print(int(a1),type(int(a1)))
# # 整数转换成浮点数
# print(float(b1),type(float(b1)))

# 数字的常用函数
# abs绝对值
a2 = -3
# print(abs(a2))

# 向上取整  ceil  天花板  操作小数
# 向下取整  floor  地板
# 输入math进行导包  alt+enter

import math

a3 = 1.2
# print(math.ceil(a3))
# print(math.floor(a3))

# 保留几位小数  round  格式定义：round(数字，保留位数)
# print(round(3.14151617,3))

# 随机数   在区间内任意输出一个数  random
# # 1.导包
# import random
# # random   默认输出0到1的随机任意数,小数
# print(random.random())
# # randint（a,b）区间数字随机数，区间只能是整数
# print(random.randint(0,20))

# 字符串   定义：通过单引号，双引号，三引号    ‘xxx’   "xxx"  '''xxxx'''
str1 = '小明'
str2 = "小明"
str3 = '''小明'''
# print(str1,type(str1))
# print(str2,type(str2))
# print(str3,type(str3))

# 字符串的切片   作用：由一个大的字符串切成一个小的字符
# 格式：str[开始值：结束值：步长]  开始值：从0开始，结束值是左闭右开，步长就是间隔，默认1
# 从左向右取  0开始取，  从右向左取，则从-1开始取
str4 = 'python123'
# 输出thon
# print(str4[2:6])
# # 输出123
# print(str4[6:9])
# print(str4[6:])
# print(str4[-3:])
# # 输出最后一个字符3
# print(str4[-1])
# # 隔一个字符取一个,每两个取一个
# print(str4[::2])

# 字符串的反转
str4 = 'python123'
# print(str4[::-1])

# 字符串和数字是不可变的，a变化  但内存地址没有变，只是两个值都叫a，id()内存地址
a = 'abc'
# print(a,id(a))
b = 'abc'
# print(b,id(b))

# 字符串中运算符   +拼接   *复制
str5 = 'a'
# 拼接
# print(str5 + 'b')
# 复制
# print(str5*2)

# 特殊字符   \n 换行   \t 制表符，可以进行缩进
# \n 换行
str6 = 'abc\n123'
# print(str6)
# \t 制表符，可以进行缩进
str7 = '\t123456'
# print(str7)

# 反斜杠 \   常用于路径，反斜杠是关键字，想要地址输出，有两种方式，一再加1个\，二加个r
# 一：再加1个斜杠  \
str8 = 'D:\\vipproject\class02\demo02.py'
# print(str8)
# 二：前面加个r
str8 = r'D:\vipproject\class02\demo02.py'
# print(str8)

# 字符串格式化 格式化传内容进去
# 1，通过占位符进行占位  %s  字符   %d  数字类型  %f 浮点类型
# print('%s真漂亮，今年%s岁'%('秋水',18))

# 2，format格式占位
# print('{}真漂亮，今年{}岁'.format('秋水',20))

# 3，还可以指定顺序执行
# print('{0}真漂亮，今年{1}岁'.format('秋水',20))

# 4,f-string
name = '虚竹'
age = 5
# print(f'{name}真漂亮,今年{age}岁')

# 字符串的分割和连接  split   join
# split 分割  格式:split(分割的内容,次数)
str9 = '   abcgbsbfbfhybdfg'
str10 = 'ab\ncgbsbf\tbfhybdfg'
# split()分割空白或者说对\t \n 进行分割
# print(str9.split())
# print(str10.split())
# 填充内容分割 split('b',6)
# print(str10.split('b',6))

# join 连接
str10 = '111'
str11 = 'ssss'
# print(str10.join(str11))

# 字符串的内置函数
str12 = 'xiaoming123'

# replace 替换
# print(str12.replace('xiaoming','小明'))

# len  统计字符串长度
# print(len(str12))

# find  查找字符串  格式: find(str,开始索引,结束索引)
str13 = 'assdwfdfgrsnyn'
# 找到返回索引
# print(str13.find('s'))
# print(str13.find('s',3))
# 没有找到返回-1
# print(str13.find('s',20))

str13 = 'ssdwfdfgrsnyn'
# isalnum  判断是字母
# print(str13.isalnum())
# isnumeric是数字
# print(str13.isnumeric())
# islower是小写
# print(str13.islower())

# 常见的字符串大小写转换
str14 = 'qAASDFfdfgrsnyn'
# upper  转换成大写
# print(str14.upper())
# lower  转换成小写
# print(str14.lower())
#capitalize  只首字大写
# print(str14.capitalize())
# swapcase  大小写互换
# print(str14.swapcase())


# 元组：不可变数据类型  tuple
# 定义：（）表示，数据是可以放任意类型的数据，数据之间 ， 隔开

# 创建一个空元组
a = ()
# print(a,type(a))

# 元组里面放数据
a1 = (1,2,3,True,'aaa',[1,2])
print(a1,type(a1))

# 在元组中放一个数据，在数据后面加个逗号，，不加逗号，python会认作数学中的（）
a2 = (1,)
# print(a2,type(a2))

# 取值 ‘aaa’,下标取值，从0开始
a3 = (1,2,3,True,'aaa')
# print(a3[4])

# 元组支持切片 [:]，左闭右开，获取2，3
a4 = (1,2,3,True,'aaa')
# # 第一种：
# print(a4[1:3])
# # 第二种：
# print(a4[-4:-2])
# # 第三种：
# print(a4[-3:-5:-1])

# 元组不可以进行增删改，是不可变数据类型，只能通过拼接方式增加数据
a5 = (1,2,3,True,'aaa')
a6 = (False,)
# print(a5+a6)

# 复制*
# print(a6*2)














