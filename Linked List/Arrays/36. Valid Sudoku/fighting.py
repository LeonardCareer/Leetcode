class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        lines = board
        colunm = [[] for i in range(9)]
        grid = [[] for i in range(9)]

        for i in range(len(lines)):
            for j in range(len(lines[0])):
                colunm[j].append(lines[i][j])
                index = (i // 3) * 3 + (j // 3)
                grid[index].append(lines[i][j])

        def check(temp: list[list[str]]):
            for i in temp:
                if len(set(i)) != len(i) - i.count(".") + 1:
                    return False
            return True

        return check(lines) and check(colunm) and check(grid)


temp = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(temp.isValidSudoku(board))
