'''
给定一个排序数组和一个目标值,在数组中找到目标值,并返回其索引
如果目标值不存在于数组中,返回它将会被按顺序插入的位置
示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1
'''
class Solution():
    def searchInsert(self,nums,target):
        #target大于整个列表
        if nums[-1] < target:
            s1 = len(nums)
        #target小于整个列表
        elif nums[0] > target:
            s1 = 0
        else:
            for i in range(len(nums)):
                #列表中没有元素与target相等
                if nums[i] < target < nums[i+1]:
                    s1 = i + 1
                #列表中存在元素与target相等
                elif nums[i] == target:
                    s1 = i
        return s1
li = Solution()
lo = li.searchInsert([1,3,5,6],0)
print(lo)