class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        self.num = 0
        self.visited: List[Tuple[int, int]] = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x,y) not in self.visited:
                    self.num += 1
                    self.dfs(x, y, grid)
        return self.num

    def dfs(self, x: int, y: int, grid: List[List[str]]):

        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
            return

        if grid[x][y] == "0" or (x, y) in self.visited:
            return

        self.visited.append((x, y))
            
        self.dfs(x, y+1, grid)
        self.dfs(x+1, y, grid)
        self.dfs(x, y-1, grid)
        self.dfs(x-1, y, grid)



