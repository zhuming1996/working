class Hero():        #创建类
    def move(self):         #定义一个方法
        print("------正在前往事发地------")

hero = Hero()          #创建对象，实例化对象

#给对象添加属性
hero.name = "luky"             
hero.hp = 2500


print(f"{hero.name}英雄的生命值是{hero.hp}")
hero.move()        #调用实例化对象

#实例化属性只有对象能访问到，类无法访问到