class Firearms():      #创建类
    def __init__(self,name,model,count):    #初始化对象属性
        self.name = name
        self.model = model
        self.count = count
    def shoot(self):                #定义方法
        if self.count <= 0:
            print("------抱歉，没有子弹啦!!!!!")
        else:
            print(f"{self.name}使用的枪械是{self.model},还剩下{self.count}颗子弹")
            self.count -= 1

A = Firearms("王天","AK47",3)    #创建实例化对象
A.shoot()       #调用方法
A.shoot()
A.shoot()
A.shoot()
