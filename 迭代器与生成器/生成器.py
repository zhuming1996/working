#得到生成器()
# s1 = (k*2 for k in range(10))

#运行生成器得到数据
#方法一：__next__()
# s2 = s1.__next__()
# print(s2)


#方法二：next()
# s3 = next(s1)
# print(s3)


#超过取值范围，抛出异常StopIteration
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))



#函数做为一个生成器,只要函数中出现了yield关键字，函数就变成生成器了
def func():
    n = 0
    while True:
        n += 1
        yield n
        
k1 = func()
print(next(k1))
print(next(k1))
