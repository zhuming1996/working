'''
扩展父类的方法
'''
#方法一：父类名.方法（self）
# class Animal():
#     def eat(self):
#         print("吃东西")
# class Dog(Animal):
#     def eat(self):
#         Animal.eat(self)       #父类名.方法（self）
#         print("啃骨头") 
# A = Dog()
# A.eat()

class Human():
    def __init__(self,name):
        self.name = name
    def note(self):
        print(f"{self.name}正在吃早饭")
class Stick(Human):
    def note(self):
        Human.note(self)
        print(f"{self.name}正在吃包子")
ac = Stick("嗨嗨")
ac.note()        

#方法二：super().父类方法
# class Animal():
#     def __init__(self,name):
#         self.name = name
#     def black(self):
#         print(f"{self.name}在叫")
#         print("哈哈")

# class white(Animal):
#     def black(self):
#         super().black()       #扩展父类的方法
#         print(f"{self.name}在汪汪叫")
#         print("嘿嘿")

# de = white("小白")
# de.black()

class BUy():
    def __init__(self,name,mode):
        self.name = name
        self.mode = mode
    def Go_to_work(self):
        print(f"{self.name}选择{self.mode}方式去上班")
class Buy(BUy):
    def Go_to_work(self):
        super().Go_to_work()
        print(f"{self.name}被迫选择了{self.mode}的方式去上班")
ab = Buy("王五","地铁")
ab.Go_to_work()
