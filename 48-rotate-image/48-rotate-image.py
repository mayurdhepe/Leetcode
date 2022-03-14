class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # transponse the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i],  matrix[i][j] =  matrix[i][j],  matrix[j][i]
        
        # flip the first and last columns
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j],  matrix[i][n-1-j] =  matrix[i][n-1-j],  matrix[i][j]
                
        
        return matrix
                
        
        
        