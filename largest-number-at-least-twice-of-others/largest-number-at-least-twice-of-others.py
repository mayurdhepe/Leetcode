import math
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxIndex = -1
        maxNum = -1
        for i, num in enumerate(nums):
            if num > maxNum:
                maxNum = num
                maxIndex = i
                
        for i, num in enumerate(nums):
            if num != maxNum and maxNum < 2*num:
                return -1
            
        return maxIndex
            