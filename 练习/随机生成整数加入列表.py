
#随机生成8个1-20之间的随机整数，保存到列表中，打印
import random
# list1 = []
# for n in range(8):
#     m = random.randint(1,20)
#     list1.append(m)
#     list1.sort()
# print(f"未增加之前的列表是：{list1}")
# a = random.randint(1,10)
# list1.append(a)
# list1.sort()
# print(f"增加的整数是：{a}，列表是{list1}")

class Math():
    def __init__(self,n,m,a,b):
        self.a = a
        self.b = b
        self.n = n
        self.m = m
    def reedom(self):
        list1 = []
        for i in range(8):
            b = random.randint(self.n,self.m)
            list1.append(b)
            list1.sort()
        print(f"未增加之前的列表是：{list1}")
        return list1
class Math1(Math):
    def haha(self):
        list2 = Math.reedom(self)
        e = random.randint(self.a,self.b)
        list2.append(e)
        list2.sort()
        print(f"增加的整数是：{e}，列表是{list2}")
        return list2
        

th = Math1(1,20,1,10)
print(th.haha())
        
        
        

