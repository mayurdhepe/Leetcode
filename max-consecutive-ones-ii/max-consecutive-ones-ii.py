class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxFlips = 1
        i, j = 0, 0
        numZeroes = 0
        maxOnes = 0
        while j < len(nums):  # while our window is in bounds
            if nums[j] == 0:   # add the right most element into our window
                numZeroes += 1
                
            while numZeroes == 2:   # if our window is invalid, contract our window
                if nums[i] == 0:
                    numZeroes -= 1
                i += 1
                
            maxOnes = max(maxOnes, j-i+1)   # update our longest sequence answer
            j += 1    # expand our window
            
        return maxOnes
            
                
                
        