class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # n ^ 0 = n
        res = 0 
            
        for n in nums:
            res = res ^ n
        
        return res