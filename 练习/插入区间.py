'''
给你一个无重叠的,按照区间起始端点排序的区间列表intervals,其中intervals[i]=[starti, endi]
表示第i个区间的开始和结束,并且intervals按照starti升序排列.
同样给定一个区间newInterval = [start, end]表示另一个区间的开始和结束.
在 intervals 中插入区间 newInterval,使得intervals依然按照starti升序排列,
且区间之间不重叠（如果有必要的话,可以合并区间）.
返回插入之后的 intervals.
注意 你不需要原地修改 intervals.你可以创建一个新数组然后返回它.
'''
class Solution():
    def functionInsert(self,intervals,newIntervals):
        list1 = []
        intervals.append(newIntervals)
        intervals.sort()
        for m in intervals:
            if not list1 or list1[-1][1] < m[0]:
                list1.append(m)
            else:
                list1[-1][1] = max(m[1],list1[-1][1])
        return list1
li = Solution()
lo = li.functionInsert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
print(lo)