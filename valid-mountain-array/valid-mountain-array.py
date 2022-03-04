class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if not arr or len(arr) < 3:
            return False
        
        increasing = arr[1] > arr[0]
        # mountain must atleast start in an increasing manner
        if not increasing:
            return False
        
        # iterate from 1 to arr.len
        for i in range(1, len(arr)):
            # equal values then not a mountain
            if arr[i] == arr[i-1]:
                return False
            
            if increasing:
                # if we reached the peak i.e.
                if arr[i] < arr[i-1]:
                    increasing = False
            else:
                # now every element must be decreasing, otherwise return false
                if arr[i] > arr[i-1]:
                    return False
        
        # we can't just return true, we must ensure that a peak was reached at some point.
        return not increasing
    
            
        
        