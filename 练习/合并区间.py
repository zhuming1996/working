class Solution:
    def merge(self, intervals):
        list1 = []
        intervals.sort()
        for m in intervals:
            if not list1 or list1[-1][1] < m[0]:
                list1.append(m)
            else:
                list1[-1][1] = max(list1[-1][1],m[1])
                # print(list1)
        return list1

li = Solution()
# lo = li.merge([[1,3],[2,6],[8,10],[15,18]])
# lo = li.merge([[1,4],[4,5]])

# lo = li.merge([[1,4],[0,4]])
# lo = li.merge([[1,4],[0,5]])


# lo = li.merge([[1,4],[2,3]])
# lo = li.merge([[4,5],[1,4],[0,1]])

lo = li.merge([[2,3],[4,6],[5,7],[3,4]])


print(lo)
