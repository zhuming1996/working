'''
应用场景：
    当父类的方法不能满足子类的需求时，可以对方法进行重写
    1、覆盖父类的方法：在子类中定义一个和父类同名的方法来实现
    2、对父类的方法进行扩展：在子类中重写父类方法，super().父类方法
'''
#覆盖写--重写
class Human():
    def __init__(self,name):
        self.name = name
    def eat(self):
        a = 1
        print(f"{self.name}在吃饭")

class zs(Human):
    def eat(self):
        a = 1
        print(f"{self.name}正在慢慢的吃饭")
        
