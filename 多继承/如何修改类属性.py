
class Human():
    age = 20    #类属性
    @classmethod
    def human(cls,age):
        cls.age = age
        return cls.age      #类名.属性来操作类属性
    
#实例化对象

p = Human()
# print(p.age)
print(p.human(18))

