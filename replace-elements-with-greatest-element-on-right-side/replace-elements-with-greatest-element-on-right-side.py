import math
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 
        n = len(arr)
        maxVal = -1
       
        for i in range(n-1, -1, -1):
            # Keep track of the 'would be' highest number
            tempMaxVal = max(maxVal, arr[i])
            # Replace the index with the last known highest number
            arr[i] = maxVal
            # Replace the last known highest number with the current highest number
            maxVal = tempMaxVal
            
        return arr
            
            
        