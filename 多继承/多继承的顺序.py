#如果不同的父类中存在同名的方法，子类对象在调用方法时，会调用哪一个类中的方法呢
class A():
    def test(self):
        print("这是A")

class B():
    def test(self):
        print("这是B")

class c(A,B):
    def play(self):
        print("这是C")
ac = c()
ac.test()    #谁先继承，先调用谁（c，a，b）