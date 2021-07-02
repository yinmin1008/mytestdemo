# 函数：就是把具有独立功能的代码块，组织成一个小模块
'''

函数：两个步骤：
    1，定义函数--封装成一个独立的功能
    2，调用函数--享受  封装的成功
函数的作用：
    可以提高编码的效率--重用
函数的格式：

def 函数名（）：
    封装的代码
    :return

调用函数的格式：
函数名（）
注意：def 关键字必须要填，函数名，随意命名，见名知意，不能已数字开头，不能以关键字命名

'''

# 封装函数
def say_hello():
    print('hello 1')
    print('hello 2')
# 调用函数   只有调用函数，函数才会被执行
# say_hello()

# 练习：实现两个函数的求和功能，并传参实现
def sum(a,b):
    resut = a+b
    print(resut)
# sum(10,30.5)

# 参数的作用：针对不同的数据进行相同的逻辑处理
#扩充：函数中的参数叫形参，调用里面叫实参

# 完整的函数，实际上会有返回值关键字 return
# 在开发的过程中，有时候我们会需要一个函数运行的最终结果，这个结果就可以通过return返回回来
def sum(a,b):
    return a+b
res = sum(30,40)
# print(res)

# 空函数：是一个完整的函数，没有实际的意义，预留一个位置
def empty():
    pass

# 函数的参数：必须参数，关键字参数，默认参数，不定长参数

# 必须参数：必须以正确的顺序传入参数，调用的时候必须和申明的一致
# 定义一个人：
def person(name,age):
    return '我是{},今年{}岁'.format(name,age)
res1 = person('小明',18)
# print(res1)

# 关键字参数：可以通过关键字传参，不用按照顺序去写
def person(name,age):
    return '我是{},今年{}岁'.format(name,age)
res2 = person(age=18,name='小明')
# print(res2)

# 默认参数：在定义的过程中设置默认值
def person(name,age=100):
    return '我是{},今年{}岁'.format(name,age)
res3 = person(name='小明')
# print(res3)

# 如果位置参数和关键字参数同在，方法函数定义时，要先写位置参数，再写默认参数
def person(name,age=100):
    return '我是{},今年{}岁'.format(name,age)
res4 = person(name='小明')
# print(res4)

# 不定长参数：在定义的过程中不知道有多少个参数，设置成不定长度的参数
# 不定长参数有两种写法： *   **
# 在参数前面带一个 *，就是把参数放在元组里面
def person(*args):
    print(args)
# person('徐州',90,'男')

# * 可单独出现，在调用的时候通过关键字调用
def a(num1,num2,*,num3):
    print(num1+num2+num3)
# a(1,2,num3=3)

def a2(a,b,c):
    print(a)
    print(b)
    print(c)
d =  (1,2,3)
# a2(*d)

# 在参数前面带两个 **，可以传多个参数，参数是关键字传参，保存在字典中
def a3(**kwargs):
    print(kwargs)
# a3(name='掌声',age=20)

# *和**同时存在，在函数的参数中*args把数据转成元组的形式，**kwargs把数据转成字典的形式
def a4(*args,**kwargs):
    print(args)
    print(kwargs)
# 这是普通参数，args可以接受多个参数
# a4(1,2,3,{'name': '秋水', 'age': 200})
# 想要把1，2，3传给*args,{'name': '秋水', 'age': 200}传给**kwargs，**必须用关键字形式传参
# a4(1,2,3,name='秋水',age=400)

# 打印中加 *，是把数据解包，会按照一定的格式去解析数据，*是解析元组，**是解析字典
def a5(*args,**kwargs):
    print(args)
    print(kwargs)
a1 = (1,2,3)
# a2 = {'name': '秋水', 'age': 20}
# * 和 **就是解包   *a1：1，2，3    **a2：name='秋水',age=420
# a5(*a1,**a2)
# a5(a1,a2)

def a6(a,b,c):
    print(a)
    print(b)
    print(c)
args = (1,2,3)
# a6(*args)

kwargs = {'a':'秋水','b':20,'c':'女'}
# a = 秋水  b = 20   c = 女
# a6(**kwargs)

# 函数嵌套：函数中嵌套函数
def test1():
    print('+'*50)

def test2():
    print('-'*50)
    test1()
    print('-'*50)

# test2()

# 匿名函数：lambda 表达式
# 语法：lambda 参数，参数：表达式

# 普通函数求和
def sum(a,b):
    print(a+b)
# sum(1,3)

# 匿名函数求和
sum = lambda a,b:a+b
# print(sum(2,3))


# 模块：就是py文件，想用另一模块中的方法，要先拿模块，再调用里面的方法





