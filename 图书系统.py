# class LibraryManagementSystem():
list1 = [
        # {
    #     # {"书名":"西游记","作者":"吴承恩","出版社":"人民出版社","价格":"31.00"},
    #     # {"书名":"三国演义","作者":"罗贯中","出版社":"北京出版社","价格":"33.00"},
    #     # {"书名":"水浒传","作者":"施耐庵","出版社":"上海出版社","价格":"24.00"},
    #     # {"书名":"红楼梦","作者":"曹雪芹","出版社":"浙江出版社","价格":"39.00"}
    # }
    ]
    
    # def column(self):
nums = int(input("欢迎来到图书馆,请选择你需要的功能：\n1 添加书本\n2 借书\n3 还书\n4 查询\n5 查看所有图书\n6 退出\n"))
if nums == 1:
    print("请输入图书的信息:")
    while True:
        dict2 = {}
        a = input("书名:")
        dict2["书名"] = a
        b = input("作者:")
        dict2["作者"] = b
        c = input("出版社:")
        dict2["出版社"] = c
        d = input("价格:")
        dict2["价格"] = d
        list1.append(dict2)
        con = input("录入成功,是否继续录入图书:\n1 继续添加\n2 退出\n")
        if con == 1:
            a = input("书名:")
            dict2["书名"] = a
            b = input("作者:")
            dict2["作者"] = b
            c = input("出版社:")
            dict2["出版社"] = c
            d = input("价格:")
            dict2["价格"] = d
            list1.append(dict2)
        else:
            break
        # print(list1)
            
        
