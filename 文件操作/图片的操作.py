
#读取图片
with open(r"C:\Users\Administrator\Desktop\pic.jpeg",'rb') as f:
    pic = f.read()

    
#将读取到的内容写入到文件
with open(r"图片.jpeg",'wb') as file:
    file.write(pic)