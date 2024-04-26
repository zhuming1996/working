class MyClass():       #创建类
    def __init__(self,name,age):
        self.name = name    #添加类的属性
        self.age =age       #添加类的属性
    def SayHello(self):            #定义方法
        print(f"你好，{self.age}岁的{self.name}同学")
        
A = MyClass("luky",20)    #创建对象，实例化对象
A.SayHello()     #调用方法