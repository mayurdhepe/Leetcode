class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        ans = 0 
        mod = (10 ** 9) + 7
        n = len(arr)
        arr.sort()
        
        mp = {}
        
        for i in range(n):
            # leaf node
            curr_ans = 1
            
            for j in range(i):
                if arr[i] % arr[j] > 0:
                    continue
                    
                num1 = arr[j]
                num2 = arr[i]//arr[j]
                
                # n = p * q
                # p = num of trees from by p,  # q = num of trees from by q
                if num1 in mp and num2 in mp:
                    curr_ans = (curr_ans + (mp[num1] * mp[num2]) % mod) % mod
                
            mp[arr[i]] = curr_ans
            ans = (ans + curr_ans) % mod
            
        return ans 
                
        