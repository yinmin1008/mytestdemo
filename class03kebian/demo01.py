# 可变数据类型   字典 dict   列表 list   集合 set

# 列表 list ：是一种有序的集合，对数据进行增删改，使用最频繁的一种数据类型
# 定义：[] 进行标识，数据任意类型，用逗号隔开
# 创建一个空列表
list0 = []
# print(list,type(list))

list1 = [1,2,3,'abc',(2,3,'as')]
# print(list1,type(list1))

# 获取列表中的数据  通过下标取值，支持切片
list2 = [1,2,3,'abc',(2,3,'as')]
# 获取‘abc’
# print(list2[3])

# 获取后两个值
# print(list2[3:])

# 对于列表进行增删改
# 增加数据  append()往末尾增加数据   insert()指定位置加数据  extend()末尾加数据
list3 = [1,2,3,'abc',(2,3,'as')]
# append()往末尾增加数据
list3.append('10')
# print(list3)
# insert()指定位置加数据
list3.insert(0,'啦啦啦')
# print(list3)
# extend()末尾加数据，拆分成单个字符
list3.extend('快捷键')
# print(list3)

# append()和extend()追加多个数据，append()后面直接追加数据 ，extend()拆分数据插入
list3.append([1,2,3])
# print(list3)
list3.extend([1,2,3])
# print(list3)

# 修改
list4 = [1,2,3,'abc',(2,3,'as')]
# 把abc改为 ABC，通过索引进行修改
list4[3] = 'ABC'
# print(list4)

# 删除 pop索引删除   remove指定数据删除  del删除一个或者连续几个元素或者整个元素删除
list5 = [1,2,3,(2,3,'as'),'abc']
# pop通过索引删除，并且删除会返回删除的数据
# a = list5.pop(0)
# print(a)
# print(list5)
# pop是可以不填参数的，默认删除最后一个
# b = list5.pop()
# print(b)
# print(list5)
#remove删除，通过元素删除  （）里面一定要填数据  remove删除不会返回删除的数据
# print(list5.remove(3))
# print(list5)

# del删除一个或者连续几个元素或者整个元素删除,支持切片
list6 = [1,2,3,'abc',(2,3,'as')]
del list6[1]
# print(list6)
# 支持切片几个元素
del list6[0:2]
# print(list6)
# 删除整个元素
del list6
# print(list6)

# 重复元素删除
list7 = [1,3,3,3,'abc',(2,3,'as')]
# 统计一下重复的元素  count(数据)
# print(list7.count(3))

# 找到重复数据2的下标进行删除，找重复数据2  可以用find和index(找的值，开始下标，结束下标)，
# 区别：find没找到返回-1，index没找到会报错
# print(list7.index(3,0,len(list7)))
# 删除，下标
# print(list7.pop(2))
# print(list7)
# 直接打印出重复数值
# print(max(list7,key=list7.count))

# list运算符+ *
list7 = ['abc',(2,3,'as')]
list8 = [1,2,3,3]
# print(list7+list8)
# print(list7*2)


# 其他操作
list9 = [9,4,3,5,7]
# 排序  升序：sort
list9.sort()
# print(list9)
# 降序
list9.sort(reverse=True)
# print(list9)
# 翻转
list9.reverse()
# print(list9)

# 数据类型转换
# 元组转为列表
a =(1,2,3)
# print(list(a),type(list(a)))
# 列表转为元组
b = [1,2,3]
# print(tuple(b),type(tuple(b)))

# 字典：也是用来存储数据，除了列表以外，最灵活的数据
# 定义：{key1:value,key2:value,}  key1键，value值  键值对，注意：key是唯一的
# 创建一个空字典
dict1 = {}
# print(dict1,type(dict1))
# 字典中有数据
dict2 = {'name':'qiushui','age':18}
# print(dict2)

# 访问字典中的数据，通过key取值
dict3 = {'name':'qiushui','age':18}
# print(dict3['name'],dict3['age'])

# 字典进行增删改
# 增加数据  sex
dict3['sex'] = '女'
# print(dict3)

# 修改数据
dict3['name'] = '秋水'
# print(dict3)

# 删除  pop(指定key删除)  popitem() 删除最后一个  del[指定键删除]或整个
dict4 = {'name':'qiushui','age':18,'sex':'女'}
# del dict4['name']
# print(dict4)

# dict4.pop('age')
# print(dict4)

# dict4.popitem()
# print(dict4)

# dict3中更新dict4数据,key不能重复，不存在的key就新增，存在的key就更新
dict3 = {'name':'qiushui','age':18}
dict5 = {'name1':'xuzhu','age':20}
dict3.update(dict5)
# print(dict3)

# 字典转换数据类型
#字典转换成字符串
dict6 = {'name1':'xuzhu','age':20}
# print(str(dict6),type(str(dict6)))

# 字符串转换成字典   eval()
dict7 = "{'name1':'xuzhu','age':20}"
# print(eval(dict7),type(eval(dict7)))

# items  一次性拿到字典中所有的键值对
dict8 = {'name1':'xuzhu','age':20}

for i ,j in dict8.items():
    # print(i,j)
    pass

for i in dict8:
    # print(i,dict8[i])
    pass

# 创建一个新字典  formkeys(键列表，值)
list11 = ['name','age','sex']
list12 = ['秋水','18','女']
dict9 = {}
dict10 = dict9.fromkeys(list11,1)
# print(dict10)

# 集合 set:是一种无序的，无法通过下标获取
# 定义：{}或者set进行标识，数据是任意的
# 创建一个集合
set1 = {1,2,3,'ass'}
# print(set1,type(set1))
# set()里放元组或列表都可以
set2 = set((1,2,3,True,'aaa'))
# print(set2)
# list 不使用 hash 值进行索引，故其对所存储元素没有可哈希的要求；
# set / dict 使用 hash 值进行索引，也即其要求欲存储的元素有可哈希的要求

# 创建空集合，需要用set()
set3 = set()
# print(set3,type(set3))

# 访问set中的元素，不能访问，因为是无序的
# 进行增删改

# 增加
set4 = set((1,2,3,'aaa'))
# 第一种
set4.add('秋水')
# print(set4)
# 第二张
set4.update((99,8,7))
# print(set4)

# 删除  remove()指定元素删除  pop任意删除  discard指定删除  clear整体删除
# remove()指定元素删除，没有找到元素会报错
set4.remove(99)
# print(set4)
# discard指定删除，没有找到元素也不会报错
set4.discard(7)
# print(set4)
# clear整体删除
set4.clear()
# print(set4)

# 作用：对集合操作，重复值操作
# 交集&：两个集合中相同的元素
# 并集|：两个集合中所有元素去重
# 差集-：返回a所有的元素，b的元素不要
# 补集^：返回两个集合中的所有元素，重复元素不要
a = set((1,2,3,4,5))
b = set((5,6,7,8))
# print(a&b)
# print(a|b)
# print(a-b)
# print(a^b)

# 去重
c = [1,2,3,4,4,5,5,6]

for i in set(c):
    print(i)
# 不换行，后面加end=''
for i in set(c):
    print(i,end='')
# 逗号隔开，则加逗号
for i in set(c):
    print(i,end=',')