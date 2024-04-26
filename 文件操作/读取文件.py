

#读取文件
'''
    1、read(n):设置读取数据的长度，不传或传入负数表示读取全部
    2、readline():一次读取一行内容
'''
file = open('name.txt','r',encoding= "utf-8")
content = file.read()   #表示取多少个字符,不填表示全部
# content = file.readline()    #一次只读取一行
# content = file.readlines()      #把所有行一次性都获取到，已列表形式返回
print(content)

# for i in file:
#     print(file.readlines())
# file.close()
