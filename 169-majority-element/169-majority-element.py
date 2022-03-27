class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0 
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > maxCount:
                res = n
            maxCount = max(maxCount, count[n])
            
        return res
            
       
        