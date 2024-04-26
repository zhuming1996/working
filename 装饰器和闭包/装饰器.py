'''
模板
'''
#标准装饰器的模板
# def wrapper(func):
#     def inner(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res
#     return inner

#日志打印器
def loggin(func):         #func表示业务函数的函数名
    def inner(*args):
        print(f"------开始计算函数啦{func.__name__}------")
        func(*args)
        print(f"------计算结束!------")
    return inner

@loggin
def add(a,b):        #业务函数
    print(f"和是{a+b}")
    
add(100,20)
    
    