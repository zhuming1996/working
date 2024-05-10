'''
给你一个mxn的整数网格accounts，其中accounts[i][j]是第i​​​​​​​​​​​​位客户在第j家银行托管的资产数量。
返回最富有客户所拥有的资产总量 。
客户的资产总量就是他们在各家银行托管的资产数量之和。最富有客户就是资产总量最大的客户。
'''

'''
示例2:
输入:accounts = [[1,5],[7,3],[3,5]]
输出:10
解释：
第 1 位客户的资产总量 = 6
第 2 位客户的资产总量 = 10 
第 3 位客户的资产总量 = 8
第 2 位客户是最富有的，资产总量是 10
'''
class Solution:
    def maximumWealth(self, accounts):
        list1 = []
        sum = 0
        for m in accounts:
            for n in m:
                sum += n
            list1.append(sum)
            sum = 0
            max_num = max(list1)
        return max_num
li = Solution()
# lo = li.maximumWealth([[1,2,3],[3,2,1]])
lo = li.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
print(lo)
                