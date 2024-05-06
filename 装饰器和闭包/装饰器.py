'''
模板
'''
#标准装饰器的模板
# def wrapper(func):
#     def inner(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res
#     return inner
import datetime
#日志打印器
def loggin(func):         #func表示业务函数的函数名
    def inner(*args,**kwargs):
        print(f"------开始计算函数啦,当前时间是{datetime.datetime.now()}------")
        func(*args,**kwargs)
        print(f"------计算结束!当前时间是{datetime.datetime.now()}------")
    return inner

@loggin
def add(a,b):        #业务函数
    print(f"和是{a+b}")
    
add(100,20)
    
    