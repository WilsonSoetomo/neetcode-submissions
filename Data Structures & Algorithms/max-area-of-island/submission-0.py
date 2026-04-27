class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        maxy = len(grid)
        maxx = len(grid[0])

        def dfs(grid, y, x):
            if x < 0 or x >= maxx or y < 0 or y >= maxy:
                return 0
            if grid[y][x] == 0:
                return 0
            elif grid[y][x] == 1:
                grid[y][x] = 0
                return 1 + dfs(grid, y + 1, x) + dfs(grid, y - 1, x) + dfs(grid, y, x + 1) + dfs(grid, y, x - 1)

        for row in range(maxy):
            for col in range(maxx):
                res = max(dfs(grid, row, col), res)

        return res