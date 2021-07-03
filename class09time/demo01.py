
#异常：在程序运行过程中，如果报错了，就会停止，抛出错误信息
# 程序停止并且提示错误信息这个过程就叫做抛出异常

#异常：为了程序的稳定性和健壮性    异常处理：针对突发情况做集中的处理

'''
语法结构：
    try:
        尝试代码
    except:
        出现错误的处理
    except Exception as e:
        错误处理

程序中不确定会不会出现问题的代码，就写try
如果程序出现问题，就执行except里面的代码
'''

#题目：要求用户输入整数

# 用户输入  input  默认string字符串格式，int转型

# try:
#     num = int(input('请输入数字：'))
#     print(num)
# except:
#     print('请输入正确数字')

# 输入一个数字进行整除
# try:
#     num = int(input('请输入数字：'))
#     res = 2/num
#     print(res)
# except ZeroDivisionError:
#     print('不能除0')
# except ValueError:
#     print('请输入正确的数字')

from time import time

'''
类型：
    indexError   下标索引出现问题
    keyError      字典里面的键有问题
    TypeError     对象的类型有问题
    IOError       文件打开或关闭流错误有问题
'''
# 对未知的异常进行处理   Exception

# try:
#     num = int(input('请输入数字：'))
#     res = 2/num
#     print(res)
# except Exception as e:
#     print(e)

#异常可以进行传递
# def demo1():
#     a = int(input('请输入数字：'))
#     return a
#
# try:
#     res = demo1()
#     print(res)
# except Exception as e:
#     print(e)

# 异常在函数里面处理
# def demo2():
#     try:
#         a = int(input('请输入数字：'))
#         return a
#     except Exception as e:
#         return e
#
# print(demo2())

#try except 作用就是用来捕获错误信息，捕获到错误的信息，会保存在日志中

'''
完整的语法结构：   用的少
    try:
        尝试代码
    except:
        出现错误的处理
    except Exception as e:
        错误处理
    else:
        没有异常的代码会执行
    finally:
        无论程序有没有问题都会被执行
'''

'''
语法结构： raise异常，主动抛异常，用于特定的需求
需求：定义一个函数，函数提示输入用户密码
    如果用户输入的密码长度<8，抛出异常
    如果用户出入的长度>=8，返回输入的密码
'''
# def input_pwd():
#     pwd = input('请输入密码：')
#     if len(pwd) >=8:
#         return pwd
#     exx = Exception('密码错误')
#     raise exx
#
# a = input_pwd()
# print(a)

# 时间 ：用于日志，测试报告，订单生成
# 时间：时间戳--描述从某一个时间点到另一个时间相隔的描述      某个时间指的是：1970年1月1日0时0分0秒


# 导包  time
import time
import datetime
import calendar
# 获取当前时间戳
# print('当前时间戳:',time.time())

# 做日期运算
# 时间元组：用9个数字表示起来的，放在元组中，（年，月，日，时，分，秒，一周第几天（0-6，0指周一），一年的第几天，夏令时）
t = (2021,7,3,22,37,30,3,322,0)
# print(t)

# 用代码表示,(tm_year=, tm_mon=, tm_mday=, tm_hour=, tm_min=, tm_sec=, tm_wday=, tm_yday=, tm_isdst=)
# print('当前元组：',time.localtime())
# print('当前元组：',time.localtime(time.time()))

# 元组转换为时间  time.asctime()
# print('以英文的方式转换为时间：',time.asctime(time.localtime()))
# print('以英文的方式转换为时间：',time.asctime(time.localtime(time.time())))

# 时间改为系统时间   time.strftime()
# print('当前系统时间：',time.strftime('%Y-%m-%d %H:%M:%S'))

# 元组转为时间戳  time.mktime()
# 指定时间转换为时间戳  2021 3 12
# print('指定时间转换为时间戳：',time.mktime((2021,7,3,0,0,0,0,0,0)))

# 当前时间转换为时间戳
# print('当前时间转换为时间戳:',time.mktime(time.localtime(time.time())))
# print('当前时间转换为时间戳:',time.mktime(time.localtime()))

# 时间戳转为元组   time.time()时间戳
# print('当前时间戳转为元组',time.localtime(time.time()))

# 指定日期转为时间格式    2021-07-03 22:56:40   datetime 扩展
# time_str = '2021 07 03 22:56:40'
# print(datetime.datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S'))

# 日历  Calendar模块  日历年历月历

# 月历
mon = calendar.month(2021,4)
# print(mon)

# 年历
cal = calendar.calendar(2021)
# print(cal)

'''
局部变量和全局变量:
    局部变量：定义在方法中
    全局变量：定义在方法外，公共的，都可以使用
变量的生命周期：
    从函数执行开始，变量创建，函数执行完了，生命周期没了，变量就死了
'''
num = 20
def demo1():
    # 希望局部变量能修改全局变量，用关键字global
    global num
    num = 10
    print('函数demo1:',num)

def demo2():
    print('函数demo2:',num)

demo1()
demo2()

