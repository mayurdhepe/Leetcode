class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            if self.checkValid(s, word):
                ans += 1
        
        return ans
    
    # check isCharEqual
    # find lengths of matching chars
    # check length constraints
    def checkValid(self, s, word):
        i = j = 0
        
        while i<len(s) and j<len(word):
            ch1 = s[i]
            ch2 = word[j]
            
            if ch1 == ch2:
                len1 = self.getLen(s, i)
                len2 = self.getLen(word, j)
                
                if len1 == len2:
                    i = i+len1
                    j = j+len2
                    continue
                elif len1>=3 and len2<len1:
                    pass
                else:
                    return False
            
                i = i+len1
                j = j+len2
            
            else:
                return False
            
        return i == len(s) and j == len(word)
    
    def getLen(self, s, i):
        length = 1
        i+=1
        while i<len(s):
            if s[i] == s[i-1]:
                length += 1
            else:
                break
                
            i += 1
        
        return length
    
    
            
            
        