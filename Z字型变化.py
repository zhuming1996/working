'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
'''
class solution():
    
    def convert(self,str1,numRows):
        if numRows <= 1:
            str2 = str1
        elif len(str1) <= numRows:
            for n in str1:
                str2 = print(n)
        else:
            for m in range(1,numRows):
                str2 =  print(str1[2*m-2],end='')
                    
            
        return str2
li = solution()
li.convert('ABSG',3)