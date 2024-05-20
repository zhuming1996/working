'''
给你一个字符串s,由若干单词组成,单词前后用一些空格字符隔开.返回字符串中最后一个单词的长度.
单词是指仅由字母组成、不包含任何空格字符的最大子字符串.
示例1:
输入:s = "Hello World"
输出:5
解释:最后一个单词是“World”,长度为5.

示例2:
输入:s = "   fly me   to   the moon  "
输出:4
解释:最后一个单词是“moon”,长度为 4.

示例3:
输入:s = "luffy is still joyboy"
输出:6
解释:最后一个单词是长度为6的“joyboy”
'''

class Solution():
    def lengthOfLastWord(self,s):
        #分割字符串
        list1 = s.split(' ')
        #从后往前遍历列表，直到存在长度不为0，返回
        for i in list1[::-1]:
            if len(i) != 0:
                break
        return len(i)
li = Solution()
# lo = li.lengthOfLastWord("   fly me   to   the moon  ")
# lo = li.lengthOfLastWord('luffy is still joyboy')
lo = li.lengthOfLastWord('Hello World')
print(lo)        
            