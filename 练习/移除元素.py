class Solution():
    def removeElement(self,nums,val):
        if val in nums:
            nums.remove(val)
        else:
            return len(nums) 
        return len(nums)

li = Solution()
nums = [3,2,2,3]
lo = li.removeElement(nums,3)
print(lo)