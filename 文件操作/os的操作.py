import os


#返回当前路径
# dir = os.getcwd()
# print(dir)


#返回当前文件夹中的所有文件，保存在列表里
# all = os.listdir('文件操作')
# print(all)


#创建文件夹
# if not os.path.exists('../teat4'):    #判断这个路径是否存在这个文件
#     f = os.mkdir('teat4')
# print(f)


#删除文件夹

#目标文件夹下没有其他文件
# m = os.rmdir('teat2')
# print(m)


#目标文件夹不是空的
path = 'teat2'
filelist = os.listdir('teat2')
for file in filelist:
    path1 = os.path.join(path,file)
    os.remove(path1)
else:
    os.rmdir(path)
print('删除成功！')