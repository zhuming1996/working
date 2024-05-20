'''
给你一个长度为n的整数数组nums和一个目标值target.请你从nums中选出三个整数,使它们的和与target最接近.
返回这三个数的和.假定每组输入只存在恰好一个解.
'''
'''
示例 1:
输入:nums = [-1,2,1,-4], target = 1
输出:2
解释:与 target 最接近的和是 2 (-1 + 2 + 1 = 2)

示例 2:
输入:nums = [0,0,0], target = 1
输出:0
'''
from itertools import combinations
class Solution:
    def threeSumClosest(self, nums, target):
        # nums.sort()
        s1 = abs((nums[0] + nums[1] + nums[2]) - target)
        list1 = []
        dict1 = {}
        list2 = []
        for n in combinations(nums, 3):
            list1.append(n)
        list1 = list(set(list1))
        for m in list1:
            area =  abs(sum(m) - target)
            if area <= s1:
                dict1[area] = sum(m)
            else:
                return nums[0] + nums[1] + nums[2]
        print(dict1)
        for i in dict1.keys():
            list2.append(i)
        min_tar = dict1[min(list2)]
        return min_tar

li = Solution()
# lo1 = li.threeSumClosest([-1,2,1,-4],1)
# lo2 = li.threeSumClosest([0,0,0],1)
# lo3 = li.threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2)
lo4 = li.threeSumClosest([1,1,1,0],-100)
# print(lo1)
# print(lo2)
# print(lo3)
print(lo4)
            