'''
构成条件：
    1、函数中嵌套一个函数
    2、内层嵌套函数，对外部作用域有一个非全局变量的引用；
    3、外层函数的返回值是内层函数的函数名
'''

# def out():
#     global n
#     sum = n
#     def inF(n):
#         return sum+1
#     return inF   #外层函数的返回值是内层函数的函数名

'''
闭包的作用
        保存局部信息不被销毁，保证数据的安全性
'''

'''
闭包的应用：
    可以保存一些非全局变量不易被销毁，改变的数据
    装饰器
    实现数据锁定
'''


def out(m):
    n = 10
    def inner():
        print(f"inner函数是{n + m}")
    return inner

ot = out(3)
ot()