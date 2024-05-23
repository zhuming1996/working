'''
给定一个包含红色、白色和蓝色、共n个元素的数组nums ,原地对它们进行排序,
使得相同颜色的元素相邻,并按照红色、白色、蓝色顺序排列.
我们使用整数 0、1和2分别表示红色、白色和蓝色.
必须在不使用库内置的sort函数的情况下解决这个问题
示例 1:
输入:nums = [2,0,2,1,1,0]
输出:[0,0,1,1,2,2]
'''
class Solution():
    def sortColors(self,nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j],nums[i]
        return nums
li = Solution()
lo = li.sortColors([2,0,2,1,1,0])
print(lo)