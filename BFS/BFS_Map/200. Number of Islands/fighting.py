from typing import List
from collections import deque

class Solution:

    # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        def getNeighbor(i ,j):
            if 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1:
                return grid[i][j]
        def setNeighbors(i, j):
            if getNeighbor(i, j) in ["0", None]:
                return
            grid[i][j] = "0"
            setNeighbors(i - 1, j)
            setNeighbors(i + 1, j)
            setNeighbors(i, j - 1)
            setNeighbors(i, j + 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    setNeighbors(i, j)
                    count += 1
        return count

    # BFS
    def numIslands2(self, grid: List[List[str]]) -> int:
        count = 0
        def bfs(i, j):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((i, j))
            while q:
                row, col = q.popleft()
                for di, dj in directions:
                    new_i, new_j = row + di, col + dj
                    if new_i in range(len(grid)) and new_j in range(len(grid[0])) and grid[new_i][new_j] == "1":
                        grid[new_i][new_j] = "0"
                        q.append((new_i, new_j))
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count
    
test = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","0"]
]
print(test.numIslands2(grid))