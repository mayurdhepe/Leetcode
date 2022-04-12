class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for i in range(n)] for j in range(n)]
        
        rows, cols = n, n
        i, j = 0, 0
        num = 1
        
        while i<rows and j<cols:
            # traverse from left to right
            for x in range(j, cols):
                matrix[i][x] = num
                num += 1
            i += 1
            
            # traverse downwards
            for x in range(i, rows):
                matrix[x][cols-1] = num
                num += 1
            cols -= 1
            
            if i < rows:
                # traverse right to left
                for x in range(cols-1, j-1, -1):
                    matrix[rows-1][x] = num
                    num += 1
                rows -= 1
            
            if j < cols:
                # traverse upwards
                for x in range(rows-1, i-1, -1):
                    matrix[x][j] = num
                    num += 1
            
            j += 1
                
        return matrix