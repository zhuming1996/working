list1 = ["苹果","梨","梨","梨","草莓","香蕉","山竹","桃子"]
# for i in list1[::-1]:
#     if i == "梨":
#         list1.remove("梨")
# print(list1)
[list1.remove("梨") for i in list1[::-1] if i == "梨"]
print(list1)