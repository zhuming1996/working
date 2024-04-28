# import random
# list1 = []
# for i in range(10):
#     a = random.randint(1,100)
#     if a >= 70:
#         print(f"当前是第{i}次循环，数据是:{a}")
#         continue
#     else:
#         list1.append(a)
# print(list1)

# for n in range(1,10):
#     for m in range(1,n+1):
#         print(f"{n}*{m} = {n*m}",end=' ')
#     print()

# num = '5.0'
# for n in num:
#     if n.isdigit():
#         print("该数是整数")
#     else:
#         print("该数不是整数")

list1 = []
while True:
    dict1 = {}
    a = input("请输入书名：")
    dict1["书名"] = a
    list1.append(dict1)
    print(list1)
