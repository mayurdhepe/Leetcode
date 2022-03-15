from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        for t in time:
            rem = t % 60
            count[rem] += 1
            
        res = 0
       
        for key,val in count.items():
            if key == 0 or key == 30:
                # specical case of 0 and 30 => do n(n-1)/2
                res += (val*(val-1))//2
            elif key<30 and (60-key) in count:
                res += count[key]* count[60-key]
                
        return res
            
        