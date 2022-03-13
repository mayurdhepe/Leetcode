class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        print(m, n)
        while i<m and j>=0:
            print (i,j)
            if matrix[i][j] == target:
                return True
            
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
                
        return False
        
        