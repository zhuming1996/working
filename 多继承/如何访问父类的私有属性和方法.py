#子类对象可以通过父类的公有方法间接访问到私有属性或方法
class A():
    def __init__(self):
        self.num = 100
        self.__num = 200
    def __Close(self):
        print(f"父类的私有方法{self.__num}")
    def test(self):
        print(f"父类的公有方法{self.__num}")
        self.__Close()
class B(A):
    def test1(self):
        # super().test()
        print(f"子类的公有方法{self.num}")
        self.test()
        
ab = B()
# ab.test()
ab.test1()
# print(ab.num)