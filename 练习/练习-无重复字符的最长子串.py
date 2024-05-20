'''
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度
示例：
    输入：s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''
class Solution():
    global maxe
    def lengthOfLongestSubstring(self,str1):
        maxe = 0
        str2 = ''
        for i in range(0,len(str1)):
            if str1[i] in str2: 
                str2 =  '' + str1[i]
                continue
            else:
                str2 += str1[i]
                maxe = len(str2)
        return maxe

m = Solution()
print(m.lengthOfLongestSubstring('abcabcbb'))