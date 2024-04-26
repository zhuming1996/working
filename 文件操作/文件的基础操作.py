

'''
文件操作：
    1、打开文件
    2、读写操作
    3、关闭文件
'''


#操作文件的方法
#open()
#read(n):n表示从文件中读取数据的长度，没有传入默认读取全部
#write():写入文件
#close():关闭文件
#属性
#文件名.name:返回要打开的文件的文件名，可以包含文件的具体路径
#文件名.mode:返回文件的访问模式
#文件名.closed:检测文件是否关闭，关闭就返回True


file1 = open("name.txt",mode = "r",encoding= "utf-8")
print(file1)
file1.close()
