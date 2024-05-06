# list1 = [23,4,55,13,35,76,45,88,73,81]
def FindMinAndMax(numbers):
    '''
    
    '''
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i],numbers[j] = numbers[j],numbers[i]
    mins = numbers[0]
    maxs = numbers[-1]
    return mins,maxs

li = FindMinAndMax([23,4,55,13,35,76,45,88,73,81])      #传入列表，调用函数
a,b = li   #使用a，b两个数来接收元组的值
print(a,b)    #打印出最大值最大值最小值
