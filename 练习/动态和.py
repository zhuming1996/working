class Solution:
    def runningSum(self, nums):
        sum = 0
        list1 =[]
        for i in nums:
            sum += i
            list1.append(sum)
        return list1

li = Solution()
lo = li.runningSum([1,2,3,4])
print(lo)
        