class Solution():
    def multiply(self,num1,num2):
        #新建两个空列表
        list1 = []
        list2 = []
        #获取两个字符串的长度
        m = len(num1)
        n = len(num2)
        #将第一个字符串拆分存入列表1
        for i in range(m):
            s1 = int(num1[i]) * 10 ** (m-i-1)     #举例：123可以拆分成[100,20,3]
            list1.append(s1)
        #将第二个字符串拆分存入列表2
        for i in range(n):
            s2 = int(num2[i]) * 10 ** (n-i-1)
            list2.append(s2)
        #字符串的和就是两个列表元素相乘的和
        res = 0
        for i in list1:
            for j in list2:
                res += i * j
        return str(res)

li = Solution()
lo = li.multiply('123','456')
print(lo)