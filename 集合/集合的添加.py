

#向集合中添加元素,非可迭代对象（字符串、整型、布尔型、元组），可迭代对象不行（列表、字典）
set1 = {"ni","hao",1,3}
set1.add("ya")
print(set1)

set1.add((1,2,3))
print(set1)