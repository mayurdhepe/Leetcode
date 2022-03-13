from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = Counter(s)
        print(charCount)
        n = len(s)
        for i in range(n):
            ch = s[i]
            if ch in charCount and charCount[ch] == 1:
                return i
        
        return -1
        