#remove(),直接填入元素值
list1 = ["苹果","梨","梨","梨","草莓","香蕉","山竹","桃子","梨"]
# for i in list1[::-1]:
#     if i == "梨":
#         list1.remove("梨")
# print(list1)
list1[0] = '梨'
print(list1)


# #pop(),填入的是元素对应的下标
# list2 = ["苹果","梨","草莓","香蕉","山竹","桃子"]
# list2.pop(1)
# print(list2)

# #del,填入的是元素对应的下标
# list3 = ["苹果","梨","草莓","香蕉","山竹","桃子"]
# del list3[1]
# print(list3)

# #clear(),直接删除整个列表
# list4 = ["苹果","梨","草莓","香蕉","山竹","桃子"]
# list4.clear()
# print(list4)