



#排列后原列表中元素顺序发生改变.sort(reverse=False),默认是False升序排序,True是降序
list1 = [3,4,2,5,1,6,9,6,7]
list1.sort(reverse=False)
print(list1)



#排列后原列表中的元素顺序不变.sorted(reverse=False),默认是False升序排序,True是降序
list2 = [3,4,2,5,1,6,9,6,7]
list3 = sorted(list2,reverse=False)
print(list3)