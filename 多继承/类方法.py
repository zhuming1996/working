# class Tool():
#     self.age = 20    #属性
#     def funa(self):    #实例方法
#         print(123)
#类方法--针对类对象定义的方法
#在类方法内部可以直接访问类属性或者调用类方法

class 类名():
    @classmethod        #类方法的标识
    def 方法名(cls):     #第一个参数一定是cls，表示当前参数
        "方法体"
#类方法内部使用类苏醒：cls.属性
#类方法内部使用类方法：cls.类方法()
#类方法本质：将类本身作为对象进行操作的方法

#通过类方法，让类名能像实例对象一样去调用类中的方法和属性
class Human():
    age = 20    #类属性
    @classmethod
    def human(cls):
        return cls.age      #类名.属性来操作类属性
    
#实例化对象
p = Human()
# print(p.age)
p.human()