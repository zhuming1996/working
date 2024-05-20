class Solution():
    def removeDuplicates(self,nums):
        list1 = []
        for i in nums:
            if i in list1:
                continue
            else:
                list1.append(i)
        s1 = len(list1)
        return s1
li = Solution()
lo = li.removeDuplicates([0,0,1,4,1,1,2,2,3,3])
print(*lo)