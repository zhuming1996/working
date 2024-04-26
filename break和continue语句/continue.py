import random
list1 = []
for i in range(10):
    a = random.randint(1,100)
    if a >= 70:
        print(f"当前是第{i}次循环，数据是:{a}")
        continue
    else:
        list1.append(a)
print(list1)



list2 = []
i = 0
while len(list2) < 10:
    b = random.randint(1,100)
    if b >= 80:
        i += 1
        print(f"当前是第{i}次,当前取到的数据是:{b}")
        continue
    else:
        list2.append(b)
        i += 1
print(list2)



list3 = [1,2,3,4,5,1,1,2,3,8,9,11,21,22,22]
list4 = []
for n in range(len(list3)):
    for m in range(n+1,len(list3)):
        if list3[n] != list3[m]:
            continue
        else:
            list4.append(list3[n])
print(set(list4))