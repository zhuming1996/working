'''
闭包：
    1、嵌套函数
    2、内部函数引用了外部函数的变量
    3、返回值是内部函数
'''

def func1(n):
    a = 10
    def func2():
        b = a + n
        print(f"内部函数{b}")
    return func2

li = func1(5)
print(li)

li()
