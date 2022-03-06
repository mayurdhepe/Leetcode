class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
        
        m,n = len(mat), len(mat[0])
        row, col = 0, 0
        
        up = True
        result = []
        while row<m and col<n:
            # if diagonal moving up
            if (up):
                while row>0 and col<n-1:
                    result.append(mat[row][col])
                    row -= 1
                    col += 1
                    
                result.append(mat[row][col])
                # if last col then change the direction and just increment the row
                # else increment the column
                if col == n-1:
                    row += 1
                else:
                    col += 1
            # diagonal moving down
            else:
                while row<m-1 and col>0:
                    result.append(mat[row][col])
                    row += 1
                    col -= 1
                    
                result.append(mat[row][col])
                # if last row then change the direction and just increment the col
                # else increment the row
                if row == m-1:
                    col += 1
                else:
                    row += 1
            up = not up
            
        return result