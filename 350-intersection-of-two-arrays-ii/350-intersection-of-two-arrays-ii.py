class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        # map for num and its count
        hashMap = {}
        for num in nums1:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for num in nums2:
            if num in hashMap and hashMap[num] > 0:
                res.append(num)
                hashMap[num] -= 1
                
        return res
        