

#  r:read只读模式，文件必须存在，不存在则报错
# file = open("name.txt",'r',encoding='utf-8')
# content = file.read()
# print(content)


#   w：write只写模式，文件存在就会先清空文件内容，再写入添加内容，不存在则创建文件
file1 = open('name.txt','w',encoding='utf-8')
content1 = file1.write('你好')
# content2 = file1.read()
# print(content2)
file1.close()

#   +: 表示可以读写某个文件
#     使用+会影响文件的读写效率，开发过程中更多会以只读、只写的方式来操作文件
#   r+:  可读写文件，文件不存在就会报错
#   w+:  先写再读，文件存在就会重新编辑文件，不存在就创建新文件


#   r+
file3 = open('name.txt','r+',encoding='utf-8')
conent4 = file3.read()
content3 = file3.write('你好')
print(conent4)
file3.close()

#   w+
file4 = open('name1.txt','w+',encoding='utf-8')
content4 = file4.write('你好，朋友')
content5 = file4.read()
print(content5)
file4.close()

#   a: 追加模式，不存在就创建文件进行写入，存在则在原有内容的基础上追加新的内容
file5 = open('name1.txt','a',encoding='utf-8')
content6 = file5.write('\n不行')
file5.close()