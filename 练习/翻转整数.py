class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        res = -num if x < 0 else num
        return res if -2**31<= res <= 2**31-1 else 0
li = Solution()
jaj = li.reverse(-120)
print(jaj)