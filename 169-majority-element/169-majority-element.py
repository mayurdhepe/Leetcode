class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore algo
        res, count = 0, 0
        
        for n in nums:
            if count == 0:
                res = n
                
            if n == res:
                count += 1
            else:
                count -= 1
                
        return res
        
        