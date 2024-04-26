'''处理异常'''
#四种异常处理格式

'''格式一'''

'''方式一'''
# try:
#     print(a)
# except:
#     print("出现错误")
# b = 10
# print(b)

'''方式二'''
# try:
#     print(a)
# except NameError as e:
#     print(e)
# b = 10
# print(b)

'''方法三'''
# try:
#     print(a)
# except Exception as e:   #万能异常Exception，可以捕获任意异常
#     print(e)
    
'''方法四：多分枝异常'''
# try:
#     print(a)
# except NameError as e:  
#     print("有错误")
# except IOError as e:
#     print(e)
# except IndexError as e:
#     print("有错误")


'''格式二try...except...else
    else里面是只有在没有异常时才会执行的代码，不会同时执行'''
# dict1 = {"name":"张三"}
# try:
#     print(dict1["name"])        #可能存在异常的代码块
# except Exception as e:      #出现异常时执行
#     print("出现错误")
# else:    #没有异常时才会执行的代码
#     print("OK")
    
    
'''格式三try...except...finally
    finally是否有异常都会执行'''
# dict1 = {"name":"张三"}
# try:
#     print(dict1["age"])
# except Exception as e:
#     print("出现错误")
# finally:
#     print("OK")


'''格式四try...except...else...finally
'''
# dict1 = {"name":"张三"}
# try:
#     print(dict1["name"])
# except Exception as e:
#     print("出现错误")
# else:
#     print("正常")
# finally:
#     print("OK")


'''抛出异常
    步骤：1、创建一个exception(...)的对象
          2、raise 抛出这个对象'''
def user():
    pwd = input("请输入密码:")
    if len(pwd) >= 6:
        return pwd
    ex = Exception("密码长度不够")
    raise ex
try:
    puser = user()
except Exception as e:
    print(f"错误：{e}")
else:
    print("OK")