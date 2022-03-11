class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # reshaping not possible
        if m*n != r*c:
            return mat
        
        result = [[0] * c for _ in range(r)]
        print(result)
        x, y = 0, 0
        for i in range(r):
            for j in range(c):
                print(i,j)
                result[i][j] = mat[x][y]
                print(result[i])
                y += 1
                
                if y == n:
                    y = y%n
                    x += 1
                    
        return result
                
                
        