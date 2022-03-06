class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 0:
            return result
        
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        
        while i<m and j<n:
            # traverse from left to right
            for x in range(j, n):
                result.append(matrix[i][x])
            i += 1
            
            # traverse downwards
            for x in range(i, m):
                result.append(matrix[x][n-1])
            n -= 1
            
            if i < m:
                # traverse right to left
                for x in range(n-1, j-1, -1):
                    result.append(matrix[m-1][x])
                m -= 1
            
            if j < n:
                # traverse upwards
                for x in range(m-1, i-1, -1):
                    result.append(matrix[x][j])
            
            j += 1
                
        return result
                
            