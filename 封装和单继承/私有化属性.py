'''
1、类的私有属性和私有方法，都不能通过对象直接访问，但是可以在本类内部访问
2、类的私有属性和私有方法，不能被子类继承，子类也无法访问
3、类的私有属性和私有方法，往往用来处理类内部的事情，不能通过对象来处理，起到安全作用
定义私有属性和方法：
    _x   也代表私有属性或方法，实际上类对象和子类都可以访问
    __x  私有成员
    __xx__   用户名字空间的魔法对象或属性
    xx__   用于避免与python关键字的冲突
'''

class classmate():
    name__ = "luky"
    _age   = 20
    __sex  = "F"
#创建实例化对象
A = classmate()
print(classmate.name__)
print(classmate._age)

#强行获取私有属性
print(A._classmate__sex)
