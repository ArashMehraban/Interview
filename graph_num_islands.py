class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return count
        
        max_r = len(grid)
        max_c = len(grid[0])
        
        def bfs(r,c):
            if 0 <= r < max_r and 0 <= c < max_c and grid[r][c] == '1':
                grid[r][c] = '0'
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
        
        for rr in range(max_r):
            for cc in range(max_c):
                if grid[rr][cc] == '1':
                    count+=1
                    bfs(rr,cc)
        return count
        
