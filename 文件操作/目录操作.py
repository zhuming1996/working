
#导入模块
import os

#1、文件重命名os.rename(旧名字，新名字)
# os.rename("name1.txt","name3.txt")

#2、删除文件os.remove()
# os.remove("name3.txt")
#3、创建文件夹os.mkdir()
# os.mkdir("zaocan")
#4、删除文件夹os.rmdik()
# os.rmdir("zaocan")
#5、获取当前目录os.getcwd()
# print(os.getcwd())
#6、获取目录列表os.listdir()
# print(os.listdir())

#获取上一级目录的列表
print(os.listdir("../"))