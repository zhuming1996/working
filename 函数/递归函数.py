'''
如果一个函数在内部不调用其他的函数，而是调用本身的话，这个函数就是递归函数
遵循：
    1、必须要有出口
    2、每次递归向出口靠近
'''
#打印出1-10
# def test(i):
#     if i == 10:
#         print(10)
#     else:
#         print(i)
#         i += 1
#         test(i)
        
# test(1)

#求1-10的累加和
def test1(i):
    if i == 5:
        print(5)
    else:
        return i + test1(i + 1)

print(test1(1))