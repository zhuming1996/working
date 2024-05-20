'''
给你一个整数数组nums,判断是否存在三元组[nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ,
同时还满足 nums[i] + nums[j] + nums[k] == 0.请你返回所有和为 0 且不重复的三元组。
'''

'''
示例 1:

输入:nums = [-1,0,1,2,-1,-4]
输出:[[-1,-1,2],[-1,0,1]]
解释:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
不同的三元组是 [-1,0,1] 和 [-1,-1,2]
注意，输出的顺序和三元组的顺序并不重要
'''

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        #对于数组长度n,如果数组为null或者数组长度小于3，返回[]
        if n < 3:
            return []
        #对数组进行排序
        nums.sort()
        res = []
        #遍历排序后数组：
        for i in range(n):
            #因为已经排序好，所以后面不可能有三个数加和等于0，直接返回结果
            if nums[i] > 0:
                return res
            #跳过重复元素，避免出现重复解
            if i > 0 and nums[i-1] == nums[i]:
                continue
            #令左指针L=i+1，右指针R=n−1，当L<R时，执行循环
            L = i + 1
            R = n - 1
            while L < R:
                #满足三个数相加等于0，输出列表
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i],nums[L],nums[R]])
                    #判断当前数是否和下一位相同，去除重复解
                    while L < R and nums[L] == nums[L+1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R-1]:
                        R = R - 1
                    #左界加一，寻找下一个解
                    L = L + 1
                    #右界减一，寻找下一个解
                    R = R - 1
                #如果和大于0，说明右界的值过大，需要减小
                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1
                #如果和小于0，说明左界的值过小，需要增加
                else:
                    L = L + 1
        return res
            
li = Solution()
lo =li.threeSum([0,0,0])
print(lo)
                        