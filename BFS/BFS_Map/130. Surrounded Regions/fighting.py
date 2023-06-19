from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        notChange = []
        def flip(x, y):
            notChange.append((x, y))
            neighbors = [(1 + x, y), (-1 + x, y), (x, 1 + y), (x, -1 + y)]
            for dx, dy in neighbors:
                if 0 <= dx < len(board) and 0 <= dy < len(board[0]) and board[dx][dy] == "O" and (dx, dy) not in notChange:
                    flip(dx, dy)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1) and board[i][j] == "O":
                    print(i, j)
                    flip(i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i, j) not in notChange:
                    board[i][j] = "X"