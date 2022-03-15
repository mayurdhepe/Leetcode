class Solution:
    def __init__(self):
        self.memo = {}
            
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        
        return self.robFrom(0, nums)
    
    def robFrom(self, i, nums):
        
        # no more houses left to examine
        if i>=len(nums):
            return 0
        
        # return cached value if present
        if i in self.memo:
            return self.memo[i]
        
        # recursive relation
        ans = max(self.robFrom(i+1, nums), self.robFrom(i+2, nums) + nums[i])
        
        # cache for future use
        self.memo[i] = ans
        
        return ans