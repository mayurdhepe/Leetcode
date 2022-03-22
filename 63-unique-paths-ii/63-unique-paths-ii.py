class Solution:
    def __init__(self):
        self.memoizeMatrix = []
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        for r in range(0, rows):
            self.memoizeMatrix.append([-1 for c in range(0, cols)])
        
        return self.getPaths(0, 0, obstacleGrid)
    
    def getPaths(self, row, col, grid):
        if (row<0 or row >= len(grid) or col<0 or col >= len(grid[0]) or grid[row][col] == 1):
            return 0
        
        if (row == len(grid)-1 and col == len(grid[0])-1):
            return 1
        
        if self.memoizeMatrix[row][col] != -1:
            return self.memoizeMatrix[row][col]
        
        rightWays = self.getPaths(row, col+1, grid)
        downWays = self.getPaths(row+1, col, grid)
        self.memoizeMatrix[row][col] = rightWays + downWays
        
        return self.memoizeMatrix[row][col]
        
        
        
        