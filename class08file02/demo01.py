# 文件处理：文件基本操作（打开，写入，关闭）   os模块
# 文件的具体应用：txt  csv   xml

# txt文件读取
# 1，打开  open(路径，模式)
# 2，读取文件/写入文件   read()/readline()/readlines()    write
# 3，关闭

# 1，读取txt文件
# f = open('123.txt','r',encoding='utf-8')
# print(f.readlines())
# f.close()

# 把列表中的数据全部去读出来，for循环实现
f = open('123.txt','r',encoding='utf-8')
# for i in f.readlines():
#     print(i)

# 读取名字，先进行字符串分割，返回列表，再进行列表取值
# for i in f.readlines():
#     print(i.split(',')[2])
# f.close()

# with不需要关闭，获取姓名与年龄
# with open('123.txt','r',encoding='utf-8') as f:
#     for i in f.readlines():
#         print(i.split(',')[1:3])

# 2，本质是文本，文本方式，也是，隔开   excel，储存方式表格文件格式
# 读取csv，需要导包
import csv

# f = open('test.csv','r',encoding='utf-8')
#
# # 读取获得的数据是文件对象，可通过for循环读取
# print(csv.reader(f))
# for i in csv.reader(f):
#     # print(i)
# # 获取名字
#     print(i[1])

# with open('test.csv','r',encoding='utf-8') as f:
#     # print(f.readlines())
#     for i in f.readlines():
#         print(i)

# csv中写入数据
stu1 = [4,'yinmin',28,'女']
stu2 = [5,'minminzi',20,'女']

# 打开文件，a追加到 文件后面，newline表示新一行不为空
# f = open('test.csv','a',newline='')
# # 写数据
# wri1 = csv.writer(f,dialect='excel')
# wri1.writerow(stu1)
# wri1.writerow(stu2)


# xml文件的读取，和html类似
# html主要用于显示数据  html就是页面的内容，图片，输入框按钮，css，输入框按钮摆放位置，布局

# 读取xml中的数据，需要导包
from xml.dom import minidom
# 1，加载xml文件
dom = minidom.parse('stu.xml')
# 2，文件数据
root = dom.documentElement
# 获得根节点/父节点
# print(root.nodeName)

# 获得类型  节点的类型是1
# print(root.nodeType)

# 获取元素的标签的值，节点的值
name1 = root.getElementsByTagName('name')
# print(name1[0].nodeName)
# print(name1[0].firstChild.data)

# 获取属性值：getAttribute
input1 = root.getElementsByTagName('input')
# input第一个标签的属性
user = input1[0].getAttribute('username')
# print(user)

# 拿到所有学生信息
# 先拿到student
# stu = root.getElementsByTagName('student')
# print(stu)
# 再拿到学生对象里面的name,age,sex
name1 = root.getElementsByTagName('name')
age1 = root.getElementsByTagName('age')
sex1 = root.getElementsByTagName('sex')
# 所有学生信息的值，循环实现
# for i in range(2):
#     print(name1[i].firstChild.data)
#     print(age1[i].firstChild.data)
#     print(sex1[i].firstChild.data)

 # 只拿ID='S001'的信息
#  studen都拿到
stu = root.getElementsByTagName('student')
# print('获取所有学生信息%s'%stu)
# 循环,if判断
for i in stu:
    # if i.getAttribute('ID'):
    #     print('id',i.getAttribute('ID'))
    #name
    name1 = i.getElementsByTagName('name')[0]
    print(name1.firstChild.data)
    age1 = i.getElementsByTagName('age')[0]
    print(age1.firstChild.data)
    sex1 = i.getElementsByTagName('sex')[0]
    print(sex1.firstChild.data)









