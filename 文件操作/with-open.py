#with open
#作用：代码执行完，系统会自动调用f.close(),可以省略文件关闭步骤
with open('name.txt','w+',encoding='utf-8') as f:
    f.write('引用天然水')
    print("当前指标的位置：",f.tell())
    f.seek(0,0)
    print("移动后指标的位置：",f.tell())
    print(f.read())
    