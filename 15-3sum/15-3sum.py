class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        # each # in input array as the possible first value
        for i, a in enumerate(nums):
            if (i > 0 and a == nums[i-1]):
                continue
                
            # solve 2 sum for L + R by 2 pointer method  
            l, r = i+1, len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # [-2, -2, -2, 0, 0, 2, 2]
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res