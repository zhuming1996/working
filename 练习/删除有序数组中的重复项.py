class Solution():
    def removeDuplicates(self,nums):
        list1 = []
        for i in nums:
            if i in list1:
                continue
            else:
                list1.append(i)
        s1 = len(list1)
        return s1,list1
li = Solution()
lo = li.removeDuplicates([1,1,2])
print(*lo)