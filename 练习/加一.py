'''
给定一个由整数组成的非空数组所表示的非负整数,在该数的基础上加一.
最高位数字存放在数组的首位, 数组中每个元素只存储单个数字.
你可以假设除了整数0之外,这个整数不会以零开头.
'''

class Solution():
    def plusOne(self, digits):
        list1 = []
        sums = 0
        for i in range(len(digits)):
            sums += digits[i] * 10 ** (len(digits)-i-1)
        num = sums + 1
        for n in str(num):
            list1.append(int(n))
        return list1
li = Solution()
# lo = li.plusOne([1,2,3])
# lo = li.plusOne([4,3,2,1])
lo = li.plusOne([9,9,9,9,9])
print(lo)

        