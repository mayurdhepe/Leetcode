import math
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 
        n = len(arr)
        maxVal = -1
       
        for i in range(n-1, -1, -1):
            tempMaxVal = max(maxVal, arr[i])
            arr[i] = maxVal
            maxVal = tempMaxVal
            
        return arr
            
            
        