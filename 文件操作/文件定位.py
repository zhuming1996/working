


#文件指针：标记从哪个位置开始读取数据
#   1、tell():显示文件内当前位置，即文件指针的当前位置
#   2、seek(offset,whence):移动文件读取指针到指定位置
#       offset：偏移量，表示要移动的字节数
#       whence：起始位置，表示移动字节的参考位置，默认是0，0代表文件开头作为参考位置，1代表当前位置作为参考位置，2代表文件结尾作为参考位置

file1 = open('name2.txt', 'w+')
content = file1.write('cnoanvjbaov')
print("文件指针位置:", file1.tell())
file1.seek(0,0)
print("当前文件指针位置:",file1.tell())
print(file1.read())
file1.close()