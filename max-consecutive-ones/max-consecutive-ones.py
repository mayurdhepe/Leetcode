import math
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        j = 0
        maxOnes = 0
        while j<n:
            if (nums[j] == 1):
                count += 1
                maxOnes = max(maxOnes, count)
            else:
                count = 0
            j += 1
            
        return maxOnes 