

#.append()向列表末尾增加元素
list1 = [1,2,3,4]
list1.append(5)
print(list1)


#.extend()增加整个列表,或者直接用"+"
list2 = [[1,3],[6,9]]
list3 = [2,5]
list2.append(list3)
# list2.extend(list3)
print(list2)
# list2 + list3
# print(list2 + list3)