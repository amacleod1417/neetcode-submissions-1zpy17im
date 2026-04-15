from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        self.minutes = 0
        rotten = []
        
        def bfs(rotten):
            queue = deque()
            queue.append(rotten)
            print(rotten)
            newrot = []

            while queue:
                print("queue:", queue)
                coords = queue.popleft()
                print("coords",coords)
                for coord in coords:
                    x = coord[0]
                    y = coord[1]
                    print("x, y:", x, y)
                    for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            print("nx, ny:", nx, ny)
                            if 0 <= nx < ROWS and 0 <= ny < COLS:
                                if grid[nx][ny] == 1:
                                    print("now rotten")
                                    grid[nx][ny] = 2
                                    newrot.append([nx, ny])
                                    print(newrot)
                if newrot:
                    queue.append(newrot.copy())
                    newrot.clear()
                    self.minutes += 1
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 2:
                    rotten.append([x, y])

        bfs(rotten)

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    return -1

        return self.minutes