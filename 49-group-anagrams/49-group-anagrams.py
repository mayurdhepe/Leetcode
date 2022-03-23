class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Mapping = char count of each string: list of anagrams 
        res = defaultdict(list) 
        
        for s in strs:
            count = [0] * 26
            for c in s:
                # ord gives the ASCII value of char
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()
            