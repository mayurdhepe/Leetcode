class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0])-1
        
        # start search from the last element in first row
        while r >= 0 and r < len(matrix) and c >=0 and c < len(matrix[0]):
            print(len(matrix[0]))
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        
        return False
                
        