class Solution():
    def longestCommonPrefix(self, strs):
        res = ''
        for i in zip(*strs):
            temp = set(i)
            if len(temp) == 1:
                res += i[0]
            else:
                break
        return res
li = Solution()
lo = li.longestCommonPrefix(["dsssa","ajasa","ajsa"])
print(lo)
            
