import re
class Solution:
    regexIPV4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patternIPV4 = re.compile(r'^(' + regexIPV4 + r'\.){3}' + regexIPV4 + r'$')
    
    regexIPV6 = r'([0-9a-fA-F]{1,4})'
    patternIPV6 = re.compile(r'^(' + regexIPV6 + r'\:){7}' + regexIPV6 + r'$')
    
    
    def validIPAddress(self, queryIP: str) -> str:
        if self.patternIPV4.match(queryIP):
            return "IPv4"
        elif self.patternIPV6.match(queryIP):
            return "IPv6"
        
        return "Neither"
        