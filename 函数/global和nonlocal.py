#global只修改内部作用域的值并不修改外部作用域的值
# def outer():
#     num = 10
#     def inner():
#         global num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()




#nonlocal往上寻找最近的局部变量，
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()