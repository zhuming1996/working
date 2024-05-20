'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
并且每个节点只能存储一位数字
'''


class abb():
    def addTwoNumbers(self,list1,list2):
        list3 = []
        e = 0
        if len(list1) == len(list2):
            for a in range(len(list1)):
                b = list1[a] + list2[a] + e
                if b >= 10:
                    e = 1
                    list3.append(b - 10)
                else:
                    e = 0
                    list3.append(b)
        elif len(list1) < len(list2):
            for a in range(len(list1)):
                b = list1[a] + list2[a] + e
                if b >= 10:
                    e = 1
                    list3.append(b - 10)
                else:
                    e = 0
                    list3.append(b)
            for a in range(len(list1),len(list2)):
                b = list2[a] + e
                if b >= 10:
                    e = 1
                    list3.append(b - 10)
                else:
                    e = 0
                    list3.append(b)
        else:
            for a in range(len(list2)):
                    b = list1[a] + list2[a] + e
                    if b >= 10:
                        e = 1
                        list3.append(b-10)
                    else:
                        e = 0
                        list3.append(b)
            for a in range(len(list2),len(list1)):
                    b = list1[a] + e
                    if b >= 10:
                        e = 1
                        list3.append(b-10)
                    else:
                        e = 0
                        list3.append(b)
        return list3

m = abb()
print(m.addTwoNumbers([6,4,3,3,5,6,4],[4,5,6,9,9,9,3]))
        