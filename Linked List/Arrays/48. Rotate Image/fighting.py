class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n // 2):
            for column in range(row, n - 1 - row):
                firstRow, firstColumn = row, column
                secondRow, secondColumn = column, n - row - 1
                thridRow, thridColumn = n - row - 1, n - column - 1
                fourthRow, fourthColumn = n - column - 1, row

                matrix[firstRow][firstColumn], matrix[secondRow][secondColumn], matrix[thridRow][thridColumn], matrix[fourthRow][fourthColumn] = \
                    matrix[fourthRow][fourthColumn], matrix[firstRow][firstColumn], matrix[secondRow][secondColumn], matrix[thridRow][thridColumn]

temp = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
temp.rotate(matrix)
print(matrix)