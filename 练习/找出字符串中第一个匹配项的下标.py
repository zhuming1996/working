class Solution():
    def strStr(self,haystack,needle):
        s1 = -1
        # if needle in haystack:
        #     s1 = haystack.index(needle[0])
        # else:
        #     s1
        # return s1
        for m in range(len(haystack)):
            for n in range(len(needle)):
                if haystack[m] == needle[n]:
                    