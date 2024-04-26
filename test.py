# a = input("请输入一个成语：")
# b = a[::-1]
# print(b)

# 去重
# list1 = [1,2,2,3,4,5,6,4,5,6,7,8,8,9,7,10,"哈"]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)


# def chu(strum, endnum):
#     sum = 0
#     for i in range(strum,endnum):
#         if i % 15 == 0:
#             sum += 1
#         print(i, ",")
#     if sum % 10 == 0:
#         print("/n")
#     return i

# 打印出1689-2019年所有的闰年
# list3 = []
# for i in range(1689,2020):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#         list3.append(i)
# print(list3)

# 更改列表中的字段
# list4 = ["更","改","lie","表","中","的","字","duan"]
# list4[2] = "ding"
# print(list4)

#数字组合:有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# sum = 0
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a != b and b != c and a != c:
#                 print(a,b,c)
#                 sum += 1
# print(sum)

#个税计算
''' 企业发放的奖金根据利润提成.
    利润(I)低于或等于10万元时,奖金可提10%;
    利润高于10万元,低于20万元时,低于10万元的部分按10%提成,高于10万元的部分,可提成7.5%;
    20万到40万之间时,高于20万元的部分,可提成5%;
    40万到60万之间时高于40万元的部分,可提成3%;
    60万到100万之间时,高于60万元的部分,可提成1.5%;
    高于100万元时,超过100万元的部分按1%提成;
    从键盘输入当月利润I,求应发放奖金总数?
'''
# profit = float(input("请输入当月的利润："))
# bonus = 0 
# if profit < 0:
#     print("输入错误，请重新输入！！！")
# elif profit <= 100000:
#     bonus = profit * 0.1
# elif profit <= 200000:
#     bonus = 100000 * 0.1 + (profit-100000)*0.075
# elif profit <= 400000:
#     bonus = 100000 * 0.1 + 100000*0.075 + (profit-200000)*0.05
# elif profit <= 600000:
#     bonus = 100000 * 0.1 + 100000*0.075 + 200000*0.05 + (profit-400000)*0.03
# elif profit <= 1000000:
#     bonus = 100000 * 0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + (profit-600000)*0.015
# else:
#     bonus = 100000 * 0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + 400000*0.015 + (profit-1000000)*0.01
# print(bonus)

# profit=int(input('Show me the money: '))
# bonus=0
# thresholds=[100000,100000,200000,200000,400000]
# rates=[0.1,0.075,0.05,0.03,0.015,0.01]
# for i in range(len(thresholds)):
#     if profit<=thresholds[i]:
#         bonus+=profit*rates[i]
#         profit=0
#         break
#     else:
#          bonus+=thresholds[i]*rates[i]
#          profit-=thresholds[i]
# bonus+=profit*rates[-1]
# print(bonus)

#数字排序
'''输入3个数字,按照从大到小的顺序进行排列'''
# raw = []
# for i in range(3):
#     case = int(input("请输入数字:"))
#     raw.append(case)
    
# for a in range(0,len(raw)-1):
#     for b in range(a+1,len(raw)):
#         if raw[a] < raw[b]:
#             raw[a],raw[b] = raw[b],raw[a]
# print(raw)

#复制
'''将一个列表中的数据复制到另一个列表中'''
# import copy
# list1 = [1,2,3,4,["a","b","c","d"]]
# list2 = copy.copy(list1)//浅拷贝
# list2 = list1[:]//浅拷贝
# list2 = list1//浅拷贝
# list2 = copy.deepcopy(list1)//深拷贝
# print(list2)

#九九乘法表
'''输出 9*9 乘法口诀表'''
# for i in range(1,10):
#     for n in range(1,i+1):
#         print('%d*%d=%2ld ' %(i,n,i*n),end='')
#     print()

#100到200的素数
'''判断101-200之间有多少个素数,并输出所有素数判断101-200之间有多少个素数,并输出所有素数'''
# prime = []
# sum = 0
# for a in range(100,201):
#     for b in range(2,a+1):
#         if  a % 2 == 0 and a % b == 0:
#             prime.append(a)
# print(prime)

#分数归档
'''利用条件运算符的嵌套来完成此题:学习成绩>=90分的同学用A表示,60-89分之间的用B表示,60分以下的用C表示'''
# listA = []
# listB = []
# listC = []
# listD = [91,45,56,67,83,79,99,84,73,62,67,89,77,69,74,87]
# for i in listD:
#     if i < 60:
#         listC.append(i)
#     elif i <= 89:
#         listB.append(i)
#     else:
#         listA.append(i)
# print(listA,listB,listC)

#输出日期
'''输出指定格式的日期'''
# import datetime
# print(datetime.date.today())

#字符串构成
'''输入一行字符串，分别统计出其中英文字母、空格、数字和其他字符的个数。'''

# str = input("请输入字符：")
# alp = 0
# num = 0
# spa = 0
# oth = 0
# for i in range(len(str)):
#     if str[i].isspace():
#         spa += 1
#     elif str[i].isdigit():
#         num += 1
#     elif str[i].isalpha():
#         alp += 1
#     else:
#         oth += 1
# print(f"英文字母： {alp}个")
# print(f"数字： {num}个")
# print(f"空格： {spa}个")
# print(f"其他字符： {oth}个")


#列表基础
# A = [1,2,3,4,5,6]
#增加项
# A.append(7)
# print(A)

#替换项
# A[3] = 3
# print(A)

#删除项
#根据元素值来删除
# A.remove(3)
# print(A)
#根据索引删除
# del A[2]
# print(A)

# A.pop(3)
# print(A)
#删除所有的值
# A.clear()
# print(A)


#基础：猜数字
'''1-30中的随机数,有三次机会,猜中后返回值'''
# import random
# a = random.randint(1,30)
# c = 0
# while True:
#     b = int(input("请输入你猜的数字："))
#     c += 1
#     if a == b:
#         print(f"猜对了,随机数是：{a},总共用了{c}次")
#         break
#     elif a > b:
#         print("猜小了")
#     else:
#         print("猜大了")

# i = 1
# while i <= 5:
#     print("*"*i)
#     i += 1
    
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*",end = '')
#         j += 1
#     print()
#     i += 1

# import copy
# a = [1,2,"a",4]
# b = copy.deepcopy(a)
# for x in a:
#     print(id(x))
# print()
# for y in b:
#     print(id(y))
# list1 = [1,2,3,4,5,6,7,8,9]
#删除
#删除单个元素，通过下标
# del list1[0]
# print(list1)

#删除区间，通过下标
# del list1[2:5]
# print(list1)

#删除单个元素，通过下标
# list1.pop(2)
# print(list1)

#删除对应元素，通过元素的值
# list1.remove(1)
# print(list1)

#删除整个列表

# dict1 = {"姓名":"张三","年龄":18}
#修改
# dict1["姓名"] = "李四"
# print(dict1)

#增加
# dict1["性别"] = "男"
# print(dict1)

#删除
# del dict1["年龄"]
# print(dict1)

#清空字典
# dict1.clear()
# print(dict1)

#遍历字典的键
# for key in dict1.keys():
#     print(key)
    
#遍历字典的值
# for value in dict1.values():
    # print(value)
    
#遍历字典的键值对
# for item in dict1.items():
#     print(item)

#集合
# s1 = set()
# print(type(s1))

# s2 = {1,2,3,4,5,6}
# print(type(s2))

#浅拷贝
import copy
a = [1,2,3,[4,5,6],7,8]
# b = copy.copy(a)
# print(id(a))
# print(b,id(b))

#修改第一层的数据时，新数据不会发生变化
# a[1] = 3
# print(a,id(a))
# print(b,id(b))

#修改第二层的数据时，新数据也会发生变化
# a[3][1] = 4
# print(a,id(a))
# print(b,id(b))


#深拷贝
#修改第二层的数据时，新数据不会发生变化
# b = copy.deepcopy(a)
# a[3][1] = 4
# print(a,id(a))
# print(b,id(b))


#函数
# def func(a,b,c=5,*e,**f):
#     print(f"{a}")
#     print(f"{b}")
#     print(f"{c}")
#     print(f"{e}")
#     print(f"{f}")
    
# func(1,2,3,4,5,6,h=7,g=8,d=9)

# a = input("请输入：")
# b = a[::-1]
# if a == b:
#     print("是回文")
# else:
#     print("不是会问") 

# def func(x):
#     print(x)
#     return x
# num = func(2)
# print(num)   




#递归函数
# def funa(n):
#     if n > 0:
#         return funa(n-1)+n
#     else:
#         return 0

# a = funa(3)
# print(a)
'''
funa(3) = funa(2) + 3
        = funa(1) + 2 + 3
        = funa(0) + 1 + 2 + 3
'''


'''斐波那契数列'''
# def funb(m):
#     if m <= 1:
#         return m
#     else:
#         return funb(m-1)+funb(m-2)
    
#输出指定长度的斐波那契序列的值(1,10)
# list1 = []
# for i in range(1,11):
#     list1.append(funb(i))
# print(list1)
    

# nums3 = 3
# con1 = int(len(nums3) // 2)
# for n in range(len(nums3)-1):
#     for m in range(n+1,len(nums3)):
#         if nums3[n] > nums3[m]:
#             nums3[n],nums3[m] == nums3[m],nums3[n]

nums3 = 6.3
print(nums3 // 2)

# str1 = "ajaks"
# for i in str1:
#     print(i)
# print(str1[0])




    