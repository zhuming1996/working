'''
编写一个函数来查找字符串数组中的最长公共前缀.
如果不存在公共前缀，返回空字符串""。
'''
'''
示例 1:
输入:strs = ["flower","flow","flight"]
输出:"fl"

示例 2:
输入:strs = ["dog","racecar","car"]
输出:""
解释:输入不存在公共前缀.
'''

class Solution():
    def longestCommonPrefix(self, strs):
        s1 = min(strs)
        s2 = max(strs)
        for n,m in enumerate(s1):
            if m != s2[n]:
                return s2[:n]
        return s1
li = Solution()
lo = li.longestCommonPrefix(["ajssa","ajasa","ajsa"])
print(lo)
            
