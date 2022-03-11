class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        currentRow = 1
        
        while currentRow <= numRows:
            if currentRow == 1:
                result.append([1])
                
            elif currentRow == 2:
                result.append([1,1])
            
            else:
                midList = [1]
                j=0
                
                while j < (currentRow - 2):
                    # -1 gives us the previous row
                    midList.append(result[-1][j] + result[-1][j+1])
                    j += 1
                
                midList.append(1)
                result.append(midList)
            
            currentRow += 1
            
        return result