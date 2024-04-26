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

for n in range(1,10):
    for m in range(1,n+1):
        print(f"{n}*{m} = {n*m}",end=' ')
    print()