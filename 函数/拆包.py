# def func1(a,b,c=2,*args,):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     # print(kwargs)
# asd = (4,5,6,7,8)

# func1(1,2,2,*asd) #用一个*来进行拆分列表或者元组形式的参数


def func1(a,b,c=2,**kwargs,):
    print(a)
    print(b)
    print(c)
    # print(args)
    print(kwargs)
asd = {"d":1,"e":2,"f":3,"g":"你好"}

func1(1,2,2,**asd) #用一个*来进行拆分字典形式的参数