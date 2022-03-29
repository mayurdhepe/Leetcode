class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # If both strings are empty string, return False
        if not s and not t:
            return False
	    # If string already equal, return False
        if s == t:
            return False
        
        lengs = len(s)
        lengt = len(t)
		
		# If string length differ more than 1, no way for them to be one distance away
        if abs(lengs-lengt) > 1:
            return False
        
		# Create a flag `found`, this is to see if the one edit distance is found.
        found = False
        i=j=0 # i for s, j for t
        while i<lengs and j<lengt:
		    # If the corresponding character is the same, we keep checking
            if s[i] == t[j]:
                i+=1
                j+=1
			# If the corresponding character is not the same, we know something is happening. But definitely this could be the place where one distance happenning
            else:
			    # If we previously found one distance away, the two strings must be more than one distance away, return to False
                if found:
                    return False
				# If we haven't found any distance yet, and this must be the first distance. We mark it as found.
                found = True
				# If the original two strings have different length, that means the one edit distance must not be Case 3, it must be Case 1 or Case 2
                if lengs != lengt:
				    # Must be Case 1, then we ignore this added char in the first string, and compare the rest
                    if lengs > lengt:
                        i+=1
				    # Must be Case 2, then we ignore this removed char in the first string, and compare the rest
                    else:
                        j+=1
				# Case 3, two strings length are equal, we ignore unmatched char, compare the rest
                else:
                    i+=1
                    j+=1
        
        return True
        