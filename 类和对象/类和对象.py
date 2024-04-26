#对象的创建
#创建对象的格式：对象名 = 类名()      实例化一个对象
class Hero():
    def info(self):
        print(self)
        print('self各不同，对象是出处')
        
#创建对象，实例化一个对象，也可以理解为是一个对象的定义
hero1 = Hero()     #创建的对象不限制数量
hero2 = Hero()
hero3 = Hero()

hero1.info()     #调用实例化对象
hero2.info()     #调用实例化对象
hero3.info()     #调用实例化对象