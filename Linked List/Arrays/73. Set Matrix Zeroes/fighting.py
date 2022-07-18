class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRow = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0

                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        firstRow = True
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        if firstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
temp = Solution()
temp.setZeroes(matrix)
print(matrix)    
                
        