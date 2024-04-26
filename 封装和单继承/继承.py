'''
继承的特点：
    继承可以使子类具有父类的各种属性和方法，而不需要再次编写相同的代码
    如果一个类A的属性和方法可复用，则可通过继承传递给类B
    此时A为父类，B为子类
继承的优点：
    1、减少了重复的代码
    2、增加了类的耦合性
    3、使得代码更规范化，合理化
'''

class God():    #创建一个父类
    def sing(self):     #定义方法
        print("唱")
    def dance(self):     #定义方法
        print("跳")

class Person(God):       #定义子类
    def rap(self):        #定义方法
        print("RAP")

A = Person()          #创建实例化对象
A.dance()
A.sing()
A.rap() 