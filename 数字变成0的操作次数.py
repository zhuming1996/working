#给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。


class Solution:
    def numberOfSteps(self, num):
        b=bin(num)[2:]
        return len(b) + b.count('1') - 1
                        
li = Solution()
lo = li.numberOfSteps(123)
print(lo)

                
                
                    