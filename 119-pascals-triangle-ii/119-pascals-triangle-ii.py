class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalT = []
        result = []
        curr = 0
        
        while curr <= rowIndex:
            if curr == 0:
                pascalT.append([1])
            elif curr == 1:
                pascalT.append([1,1])
            else:
                i = 0
                midlist = [1] 
                while i < (curr - 1):
                    midlist.append(pascalT[-1][i] + pascalT[-1][i+1])
                    i += 1
            
                midlist.append(1)
                pascalT.append(midlist)
            
            curr += 1
        
        return pascalT[rowIndex]
        