import os


#判断是否是绝对路径
r = os.path.isabs(r'C:\Users\Administrator\Desktop\测试文件\A.png')
print('-----》',r)


e = os.path.isabs(r'../图片.jpeg')
print('----》',e)



#获取路径
path = os.path.dirname(__file__)     #获取当前文件所在文件夹的路径
print(path)


#通过相对路径得到绝对路径乐事黄瓜味.png
path1 = os.path.abspath('乐事黄瓜味.png')
print(path1)

#获取当前文件的绝对路径
path2 = os.path.abspath(__file__)
print(path2)


