class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        currSum = nums[0]
        
        for i in range(n-1):
            res.append(currSum)
            currSum += nums[i+1]
 
        res.append(currSum)
        return res
            
            