
# 面向对象
'''
    万物皆对象
    面向对象：面向对象编程---object oriented programming   简写：oop：是一种封装代码的写法
    面向对象是面向过程的基础上发展出来的，面向对象比面向过程更加灵活和有扩展性

    如：把大象装进冰箱需要几步：
        1，打开冰箱
        2，大象放进冰箱
        3，关上冰箱门

    面向过程：就是有一个需求，按照这个需求，逐步去写，独立功能封装，最后有顺序调用
        def open():
            pass
        def into():
            pass
        def close():
            pass

    面向对象： 就是把冰箱作为一个对象，或者大象作为对象都可以
        冰箱：可以打开，可以装东西，可以关闭

    面向对象：更大的封装，根据要做的事情，在一个对象中封装多个方法，主要针对于复杂的系统
    面向对象两个核心内容：1，类   2，对象
        类：是具有相同特征的或者说相同行为的事物的称
            如：鸟类--特征：有翅膀，两只脚，一双眼睛，心脏四室，提问恒定
                     行为：会飞，会吃虫
        类是抽象的，不能够直接调用，类相当于模板

        定义类：
            class 类名：
                属性：
                方法
        属性指特征，方法指作用
        方法：在类中方法会默认有self，  def open(self):
        类名：见名知意，最好是大写开头，驼峰命名

'''
# 定义猫类   属性：白色，四只脚，20斤      方法：会吃，会叫，抓老鼠
class Cat:
    color = '白色'
    foot = '四只脚'
    weight = '20kg'

    def eat(self):
        print('爱吃鱼')
    def catch(self):
        print('会抓老鼠')

# 具体到猫   变量名=类名()，即实例化
tom = Cat()

# 调用   实例类.方法名    实例类.属性名
# tom.eat()
# print(tom.weight)

# tom和jack是两只猫，内存对象不同
jack = Cat()
# print(tom)
# print(jack)


# self：代表的是实例化对象本身，谁调用就代表谁
# class Cat:
#     '''
#         类中写注释
#         这是一个猫类
#     '''
#     color = '白色'
#     foot = '四只脚'
#     weight = '20kg'
#
#     def eat(self):
#         print('%s小猫爱吃鱼'%self.color)
#     def catch(self):
#         print('%s会抓老鼠'%self.name)

# tom1 = Cat()
# tom1.name = 'tom'
# tom1.eat()
# tom1.catch()
#
# jac = Cat()
# jac.name = 'jac'
# jac.eat()
# jac.catch()

# 属性：一般写在init函数中：init是一个内置方法，专门用来定义一个类具有哪些属性的方法
# 特点：创建对象时会自动调用
# init方法内部使用格式：self.属性名=属性初始值
# class Cat:
#     def __init__(self):
#         print('这是一个初始化函数')
#         # 定义了cat类创建的所有的猫都会有这一属性nama
#         self.name = 'tom'
#     def eat(self):
#         print('%s爱吃鱼'%self.name)
#
# #实例化，具体对象
# ja = Cat()
# ja.eat()


# 不想所有的猫都叫tom，传参实现
# class Cat:
#     def __init__(self,name,color,weight):
#         print('这是一个初始化函数')
#         # 定义了cat类创建的所有的猫都会有这一属性nama
#         self.name = name
#         self.color = color
#         self.weight = weight
#     def eat(self):
#         print('%s爱吃鱼'%self.name)
#         print('%s'%self.color)
#         print('%s'%self.weight)
#
# # 具体参数
# b = ('abc','白色',20)
# a = Cat(*b)
# a.eat()

'''
内置函数：
    __init__ ：创建对象时会自动调用这个方法
    __del__  : 对象从内存中销毁之前，会被调用方法
    __str__  : 返回对象的描述信息  print函数输出
'''
# class Cat:
#     def __init__(self,name):
#         self.name = name
#         print('%s小猫来了' % self.name)
#     def __del__(self):
#         print('%s小猫走了'%self.name)
#
#     def __str__(self):
#         return '我是小猫%s'%self.name
#
# a = Cat('tom')
# print(a)












