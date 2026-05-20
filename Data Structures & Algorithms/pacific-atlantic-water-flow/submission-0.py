class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        rows, cols = len(heights), len(heights[0])

        pac = set()
        atl = set()
        both = []

        def dfs(x, y, visited):
            if x < 0 or x >= rows or y < 0 or y >= cols or (x, y) in visited:
                return

            visited.add((x, y))

            for c, d in directions:
                if 0 <= x + c < rows and 0 <= y + d < cols:
                    if heights[x + c][y + d] >= heights[x][y]:
                        dfs(x+c, y+d, visited)

            

        for i in range(cols):
            dfs(0, i, pac)
            dfs(rows - 1, i, atl)
        
        for i in range(rows):
            dfs(i, 0, pac)
            dfs(i, cols - 1, atl)
        
       
        
        for x in range(rows):
            for y in range(cols):
                if (x, y) in pac and (x, y) in atl:
                    both.append([x, y])
        
        return both




