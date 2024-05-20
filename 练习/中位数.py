import time
class Solution():
    median = 0
    def findMedianSortedArrays(self, nums1, nums2):
        global median
        nums3 =sorted(nums1 + nums2)
        print(nums3)
        con = len(nums3) % 2
        con1 = int(len(nums3) // 2)
        if con == 0:
            median = (nums3[con1-1] + nums3[con1])/2 
        else:
            median = nums3[con1]
        return nums3,median

li = Solution()
print(li.findMedianSortedArrays([1,3],[2,4,5,6]))
