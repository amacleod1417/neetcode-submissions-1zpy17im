class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for x in range(self.ROWS):
            for y in range(self.COLS):
                if grid[x][y] == 0:
                    self.bfs(x, y, grid)
        

    def bfs(self, x: int, y: int, grid: List[List[int]]):
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.ROWS and 0 <= ny < self.COLS:
                    if grid[nx][ny] > grid[x][y] + 1:
                        grid[nx][ny] = grid[x][y] + 1
                        queue.append((nx, ny))
                
            
        



        



        
            


