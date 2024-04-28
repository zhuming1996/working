class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        str1 = ''
        for n in range(0,len(s)):
            for m in range(n+1,len(s)):
            # if len(str1) == 0:
                if s[n].isdigit():
                    str1 += s[n]
                    if s[m].isdigit() is False:
                        break
            # else:
            #     if s[n].isdigit() == False:
            #         break
        return int(str1)
                        
                
li = Solution()
ki = li.myAtoi('42')
print(ki)