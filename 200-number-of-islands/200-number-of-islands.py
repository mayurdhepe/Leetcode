class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0: return 0
        nr = len(grid)
        nc = len(grid[0])
        numIslands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    numIslands += 1
                    self.dfs(grid, r, c)
                    
        return numIslands
    
    
    def dfs(self, grid: List[List[str]], r: int, c: int):
        if (r<0 or c<0 or r>= len(grid) or c>= len(grid[0]) or grid[r][c] == '0'):
            return;
        
        grid[r][c] = '0';
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)
        
        