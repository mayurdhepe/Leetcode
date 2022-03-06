class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxFlips = 1
        i, j = 0, 0
        numZeroes = 0
        maxOnes = 0
        while j < len(nums):
            if nums[j] == 0:
                numZeroes += 1
                
            while numZeroes == 2:
                if nums[i] == 0:
                    numZeroes -= 1
                i += 1
                
            maxOnes = max(maxOnes, j-i+1)
            j += 1
            
        return maxOnes
            
                
                
        