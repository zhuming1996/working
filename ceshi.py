
### if 语句的嵌套
# nums = int(input("请输入成绩："))
# if nums > 0:
#     if nums < 60:
#         print("不及格")
#     else:
#         if nums < 75:
#             print("及格")
#         elif nums < 85:
#             print("良好")
#         else:
#             print("优秀")
# else:
#     print("请重新输入")


###while循环
# import random
# list1 = []
# while True:
#     nums = random.randint(0,30)
#     if nums < 10:
#         break
#     else:
#         list1.append(nums)
# print(list1)


###for 循环

# nums = 'cnaovabv'
# for i in nums:
#     print(i,end=' ')



# list1 = []
# for i in range(10):
#     list1.append(i)
# print(list1)


###continue语句,结束本次循环
# list1 = [-1,3,-3,6,7,8]
# list2 = []
# for i in list1:
#     if i < 0 :
#         continue
#     else:
#         list2.append(i)
# print(list2)


###break语句，结束当前循环  
        


###列表的操作

##创建空列表
list1 = [1,2,3,1]

##添加元素
# list1.append(1)
# print(list1)

##把一个列表往另外一个列表中添加
# list2 = [2]
# list1.extend(list2)
# print(list1)


##统计列表元素出现的次数
# nums = list1.count(1)
# print(nums)


##统计列表中的元素和
# print(sum(list1))


##对列表进行排序
# list1.sort(reverse=True)  #默认是True表示降序，False表示升序，默认是True
# print(list1)

# sorted(list1,reverse=True)
# print(list1)


##列表推导式
# list1 = [-1,3,-3,6,7,8]
# list2 = []
# for i in list1:
#     if i < 0 :
#         continue
#     else:
#         list2.append(i)
# print(list2)
# list1 = [-1,3,-3,6,7,8]
# list2 = [i for i in list1 if i > 0] 
# print(list2)


###
# class Solution:
#     def isPalindrome(self, x: int):
#         if x >= 0 :
#             if int(str(x)[::-1]) == x:
#                 return True
#             else:
#                 return False
#         else:
#             return False
# li = Solution()
# ma = li.isPalindrome(111)
# print(ma)


