'''
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法
matrix = [[1,1,1],[1,0,1],[1,1,1]]
[[1,0,1],[0,0,0],[1,0,1]]
'''

class Solution():
    def setZeroes(self,matrix):
        #矩阵行数
        row = len(matrix)
        #矩阵列数
        col = len(matrix[0])
        #用集合存储矩阵中为0的横纵坐标
        row_zero = set()
        col_zero = set()
        #第一次遍历matrix，把元素为0的横纵坐标记录
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        #第二次遍历，置0
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
        return matrix
li = Solution()
lo = li.setZeroes([[1,1,1],[1,0,1],[1,1,1]]) 
    
    
print(lo)