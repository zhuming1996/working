'''
__str__()函数，能够在输出对象变量时，打印自定义内容
注意：
    1、__str__()函数必须返回一个字符串
    2、定义了__str__()方法，在打印对象时，默认输出该方法的返回值
'''
class A():
    mid =  "haha"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def human(self):
        print(f"你的名字是{self.name}")
    def __str__(self):
        return "你好呀"
    
a = A("小王",34)
print(a)
        