class Student():
    name = "lucy"     #属性
    def info(self):    #方法
        print(123)
        
print(Student.__dict__)   #查看类的属性
print(Student.__dict__["name"])    #查看单个属性name的内容


#增删改查类中的单个属性
Student.name = "haha"
print(Student.name)    #修改

del Student.name    #删除属性
print(Student.name)

Student.work = "heihei"
print(Student.work)   #新增没有的属性