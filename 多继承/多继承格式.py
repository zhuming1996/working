#格式
class A():
    def demo(self):
        print("这是A")

class B():
    def test(self):
        print("这是B")

class c(A,B):
    def play(self):
        print("这是C")
ac = c()
ac.play()
ac.demo()
ac.test()