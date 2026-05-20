class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        num = 0

        
        def dfs(x, y):
            if x < 0 or x > rows or y < 0 or y > cols or grid[x][y] == "0":
                return
            
            grid[x][y] = "0"

            for c, d in directions:
                if 0 <= x+c < rows and 0 <= y+d < cols:
                    if grid[x+c][y+d] == "1":
                        dfs(x+c, y+d)
                        grid[x+c][y+d] = "0"

            

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    num += 1
                    dfs(x, y)
        
        return num

            
