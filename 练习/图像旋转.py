'''
给定一个nxn的二维矩阵matrix表示一个图像.请你将图像顺时针旋转90度.
'''
class Solution():
    def rotate(self,matrix):
        for row in zip(*matrix):
            print(row)
        #     row1 = list(row[::-1])
        # matrix[:] = row1
        # matrix[:] = [row[::-1] for row in zip(*matrix)]
        # return matrix

li = Solution()
lo = li.rotate([[1,2,3],[4,5,6],[7,8,9]])
print(lo)