
# 条件判断和循环语句

# 逻辑运算符：and  or  not  两个表达式进行判断
# 1，and：两个表达式都为真的时候，才为真，否则为假
# print(40<60 and 60>40)
# print(40>60 and 60>40)

# 2，or：两个表达式只要一个条件为真，就为真
# print(40<60 and 60>40)

# 3，not：a表达式，a为真的时候，输出的就是假，全部为假的时候就为真
# print(not 70<60)

# 成员运算符： in  not in 在字符中找值    in 在...里面，  not in  不在.....里面
# 身份运算符： is  not is 对于标识符是不是同一对象   id() 内存地址

# if判断：如果条件满足的话，就这这件事情，否则，就做另外一件事，或者什么都不做
'''

if 条件：
    条件满足的事情
else:
    条件不满足的事情
'''
# 条件：如果年龄达到18岁，就允许进入网吧，否则就回家睡觉
# age = 19
# if age >= 18:
#     print('允许网吧上网')
# else:
#     print('回家睡觉')

# 对这个判断进行升级，想在控制台输出年龄  input()实现
# age = int(input('请输入年龄：'))
# if age >= 18:
#     print('允许网吧上网')
# else:
#     print('回家睡觉')

# 字符串 ’yuchen'  判断yu是否在其中，用in
# a = 'yuchen'
# if 'yu' in a:
#     print('真可爱')
# else:
#     print('真讨厌')

# 判断是不是同一个内存地址  is   内存地址不是同一个
# a = 123
# b = 123
# if a is b:
# # if '123' is '123':
#     print('我们是同一个人')
# else:
#     print('搞错了，再来')

# 多重if判断：多个条件判断
'''
if 条件1：
    执行的事情
elif 条件2：
    执行的事情
...
else:
    执行的事情
'''
# grade = int(input('请输入成绩：'))

# if grade >= 90:
#     print('你是厉害的')
# elif grade>=80:
#     print('你就是优秀的')
# elif grade >=70:
#     print('你就是中等的')
# elif grade >60:
#     print('你还需继续努力')
# else:
#     print('不及格')


# if嵌套：在条件满足的时候再加条件
# 格式：
'''
if 条件：
    if 条件：
        要执行的事情
    else:
        要执行的事情
else:
    要执行的事情
'''

# grade = int(input('请输入成绩：'))

# if grade >60:
#     if grade >90:
#         print('你是优秀的')
#     elif grade >80:
#         print('你是中等的')
#     else:
#         print('你是及格的')
# else:
#     print('你是不及格的')


# 循环：特定的一些事情重复执行
# 两种格式：while  for  
'''
while格式：
while 条件：
    循环的内容
'''

# 第一个简单的while循环    打印5次hello world
# i = 1
# while i <= 5:
#     print('hello world')
#     i = i+1

# 联系：0+1+2+3+。。。。+100

# i=0
# sum = 0
# while i <= 100:
    
#     sum = sum+i
#     i = i+1
# print(sum)

# 在循环中有break和continue
# break 当某一个条件满足时，退出循环，不执行后面的代码
# continue 当某一个条件满足时，退出循环，执行后面的代码,continue中要加逻辑

# 如：打印1-10的数字，循环7时，就不打印，不打印3
# i= 0
# while i <=10:
#     if i == 7:
#         break
#     i = i+1
#     print(i)

    
# i= 0
# while i <=10:
#     if i == 3:
#         i = i+1
#         continue
    
#     print(i)
#     i = i+1

for i in range(10):
    if i ==3:
        continue
    print(i)
    
















