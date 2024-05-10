'''
给你一个整数n,找出从1到n各个整数的Fizz Buzz表示,并用字符串数组answer(下标从1开始)返回结果,其中：
answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
answer[i] == "Fizz" 如果 i 是 3 的倍数。
answer[i] == "Buzz" 如果 i 是 5 的倍数。
answer[i] == i （以字符串形式）如果上述条件全不满足。
'''
'''
示例1:

输入:n = 3
输出:["1","2","Fizz"]

示例2:

输入:n = 5
输出:["1","2","Fizz","4","Buzz"]
'''

class Solution:
    def fizzBuzz(self, n):
        list_answer = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer = 'FizzBuzz'
            elif i % 3 == 0:
                answer = 'Fizz'
            elif i % 5 == 0:
                answer = 'Buzz'
            else:
                answer = str(i)
            list_answer.append(answer)
        return list_answer
    
li = Solution()
lo = li.fizzBuzz(3)
print(lo)