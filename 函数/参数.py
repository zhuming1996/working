#位置参数
# def sum(a,b):
#     print(a)
#     print(b)
    
# sum(1,2)

#默认参数
# def func(a,b=1):
#     print(a)
#     print(b)
# func(1)

#可变  参数
def func1(a,b,c=2,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    
func1(1,2,2,4,5,6,7,8,d=4,e=5,r='nihao')

