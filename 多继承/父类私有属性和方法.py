'''
父类私有属性和方法
不对外公开的，外界以及子类都不能直接访问
私有属性、方法通常用于做一些内部的事情
'''
#子类对象不能在自己的方法内部，直接访问父类的私有属性或私有方法
class A():
    def __init__(self,model):
        self.model = model
        self.__num = 200
    def __Close(self):
        print(f"使用了{self.model}模式，速度为{self.__num}")
class B(A):
    def __close(self):
        print(f"beiposhiyongl{self.model}")
    def close(self):
        print(f"nihaoya")
ab = B("运动")
ab.__close()   #无法访问父类中的私有方法AttributeError: 'B' object has no attribute '__close'
ab.close()
ab.__num   #无法访问父类中的私有属性AttributeError: 'B' object has no attribute '__num'
        