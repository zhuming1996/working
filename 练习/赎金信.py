'''
给你两个字符串:ransomNote和magazine,判断ransomNote能不能由magazine里面的字符构成.
如果可以,返回true:否则返回false.
magazine中的每个字符只能在ransomNote中使用一次.
'''
'''
示例1
输入:ransomNote = "a", magazine = "b"
输出:false

示例2
输入:ransomNote = "aa", magazine = "ab"
输出:false

示例3
输入:ransomNote = "aa", magazine = "aab"
输出:true
'''

class Solution:
    def canConstruct(self,ransomNote,magazine):
        list_ransomNote = [*ransomNote]
        list_magazine = [*magazine]
        for n in range(len(list_ransomNote)):
            for m in range(len(list_magazine)):
                if list_ransomNote[n] == list_magazine[m]:
                    m = m+1
li = Solution()
lo = li.canConstruct("a","b")
print(lo)