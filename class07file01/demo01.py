# 文件处理和os模块
# 为什么要学文件处理： 操作文件--打开，关闭，读取文件，写入数据

# 文件的作用：就是存储数据，方便下一次从文件中直接读取
'''
体验文件的基本操作：
    1，打开文件   open(文件路径，访问模式)   r -只读，w -只写，a -只写，
        r+:在r的基础上新增了可写的功能
        w+:在w的基础上新增了可读的功能
        a+:在写的功能上新增了可读的功能
        rb,wb用于二进制文件
    2，写入文件
    3，关闭文件
'''

# f = open('test.txt','w')
# f.write("""111
# 2222
# 33333
# """)
# f.close()

# r，如果文件不存在，会报错，只读操作，不做写入
# f = open('test1.txt','r')
# f = open('test.txt','r')
# print(f.read())
# # f.write('123')
# f.close()

# w表示只写,如果文件不存在，会新建文件写入;已存在的文件写入，会覆盖原有的内容
# f = open('text1.txt','w')
# f.write('qqq')
# f.close()

# a表示只写，文件不存在会新建文件；已存在的文件写入，会在后面追加新内容，不会覆盖原有内容
# f = open('test2.txt','a')
# f.write('cvcccccc')
# f.close()

# r+，可读可写， 没有提前创建文件，会报错，写入内容会覆盖原有的内容，r+的文件指针在开头，从头进行覆盖
# f = open('text3.txt','r+')
# f = open('test2.txt','r+')
#
# # 想知道文件指针在哪，通过tell
# print(f.tell())
#
# # print(f.read())
# f.write('aa')
# f.close()

# w+  可读又可写，  没有文件，会新建文件写入，文件指针tell,写完之后，指针在尾部，所以每次读取会读取不到内容
# 非要读取，则偏移指针位置  seek偏移实现，seek(偏移量，指针位置) 0从头开始读，偏移量可以不给
# f = open('test3.txt','w+')
# f.write('qiyshui')
# print(f.tell())
#
# f.seek(0,0)
# print(f.read())
# f.close()

# a+，可读可写  没有文件，会新建文件写入，文件指标在最后，文件存在再写入的话，会在后面新增，不会覆盖原有数据；光标再后面，所以读不到数据
# f = open('test4.txt','a+')
# # f.write('123')
# f.seek(0)
# print(f.read())
# f.close()

# 路径：
# 1，目录下的同文件，调用的话可直接使用，也可前面加 ./
# f = open('test.txt','r')
# f = open('./test.txt','r')
# print(f.read())
# f.close()

# 2，文件目录下的文件访问外层文件目录下的文件，跨目录访问，用  ../，如访问class05文件下的test文件
# f = open('../class05/test.txt','r')
# print(f.read())
# f.close()

# 3，同级目录  ./目录名/文件名


# 读取文件  read()   readline()    readlines()
# read(字符数)，不写字符数默认读全部
# f = open('test.txt','r')
# print(f.read(5))
# f.close()

# readline()  知道读取一行数据
# f = open('test.txt','r')
# print(f.readline())
# f.close()

# readlines()  读取所有数据，会配套for循环读取
# f = open('test.txt','r')
# # print(f.readlines())
#
# # 指定读取，下标读取
# # print(f.readlines()[0])
# for i in f.readlines():
#     print(i)
#
# f.close()

# with...open()as  可以不用关闭文件


'''

with open(文件路径,访问模式)as 变量:
    文件操作    
'''
# with open('test.txt','r') as f:
#     print(f.read())

# 写入
with open('test.txt','a') as f:
    f.write('123456')

# os 模块：处理文件或文件目录的
# 1，直接导入
import os
import shutil
# 路径转义：用r或者\
file1 = r'D:\vipproject\class07file01\aa'
# 创建一个文件夹
# os.mkdir(file1)

# 重命名
# os.rename(file1,r'D:\vipproject\class07file01\bb')

# 删除文件夹
# os.rmdir(file1)

# 文件夹下有文件的情况下，用rmdir删除不掉，通过shutil包下的 rmtree实现，删除非空文件
# shutil.rmtree(file1)

# 获取当前文件夹路径  os.getcwd()
# print(os.getcwd())

# 获取当前文件路径  os.path.join()
# path1 = os.getcwd()
# print(path1)
# demo = 'demo.py'
# print(os.path.join(path1,demo))

# 获取文件权限  os.access(path,mode)
# F_OK(是否存在)，R_OK(可读)，W_OK(可写)，X_OK(可执行)
file2 = r'D:\vipproject\class07file01\test.txt'
# print(os.access(file2,os.F_OK))
# print(os.access(file2,os.R_OK))
# print(os.access(file2,os.W_OK))
# print(os.access(file2,os.X_OK))

'''
正则：
    用来处理字符串
    特点：灵活性特别强
    匹配规则：\d  匹配数字  
            \w  匹配字母，数字，下划线，中文
            .   匹配任意字符，除\n以外
            ？   非贪婪模式，匹配1个或0个表达式
            +   匹配1个或多个表达式
            *   匹配0个或多个表达式
            {}  前面的元素出现的次数
'''

# 常用方法：match()   search()   findall()

# 导入正则
import re
str1 = '.123..._..wowo?开始456'

# 想要把数字匹配出来
# match（）只匹配开头，没匹配出来返回none
a = re.match('\d\d\d',str1)
a = re.match('\d{3}',str1)
a = re.match('\d+',str1)
# print(a)

# search() 只匹配一次
b = re.search('\d+',str1).group()
# print(b)

# findall()
c = re.findall('\d+',str1)
# print(c)

# 数字/字母都匹配，？不匹配
d = re.findall('[\w]+',str1)
# print(d)

# * 贪婪模式  输出 e123a123a
re1 = re.search('e.*a','bcde123a123a').group()
# print(re1)
# ？ 非贪婪模式  输出 e123a
re2 = re.search('e.*?a','bcde123a123a').group()
# print(re2)

img1 = "<img src='test.jpg' width='20px' height='30px'>"
re3 = re.search('s.*? ',img1).group()
# print(re3)


# 递归：自己调用自己
def chufa(a):
    if a == 20:
        return a
    else:
        chufa(a/2)
b = chufa(100)
print(b)















