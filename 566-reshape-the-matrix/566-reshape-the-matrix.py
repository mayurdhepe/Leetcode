class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # reshaping not possible
        if m*n != r*c:
            return mat
        
        result = [[0] * c for _ in range(r)]
       
        x, y = 0, 0
        for i in range(r):
            for j in range(c):
                result[i][j] = mat[x][y]
                y += 1
                
                if y == n:
                    y = y%n
                    x += 1
                    
        return result
                
                
        