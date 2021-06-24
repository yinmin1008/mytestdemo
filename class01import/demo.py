
# print  是打印的意思，不需要缩进
print(123)
print('你好')

# 注释：给代码起到一个备注的作用，不会运行
# 两种： 单行注释 # 快捷键 ctrl+/
#       多行注释  '''   '''  三个单引号
'''
多行注释,要英文输入法下的单引号
注意：外面是单引号，里面就要用双引号，要注意区分
'''
# 变量   作用：用来存储数据
# 格式：变量名 = 值    = 指赋值,变量名随意命名，避开关键字
a = 1


# 导入模块：有三种方式  调用某个模块下的内容/方法
# 1，import 模块名   使用格式：模块名.函数/方法
# 导入模块
import class02bukebian.demo01
# 引用
class02bukebian.demo01.test01()

# 2.from 模块名 import 函数名   使用格式：直接调用   函数/方法
# 导入模块
from class02bukebian.demo01 import test01
# 引用
test01()

# 3，from 模块名 import *    *代表该模块下全部函数/方法
# 导入模块
from class02bukebian.demo01 import *
# 引用
test01()
test02()






