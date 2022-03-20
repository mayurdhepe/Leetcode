class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        res = ""
        for i in range(len(prefix)):
            for s in strs:
                if i == len(s) or s[i] != prefix[i]:
                    return res
                
            res += prefix[i]
            
        return res
                