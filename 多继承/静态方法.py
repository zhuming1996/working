
# class A():
    
#     @staticmethod
#     def god():
#         print(123)
        
#静态方法是类中函数，它不需要实例，可以理解为是独立的单纯的函数


class Dog():
    @staticmethod
    def bark():
        print("汪汪叫")
dog = Dog()
dog.bark()