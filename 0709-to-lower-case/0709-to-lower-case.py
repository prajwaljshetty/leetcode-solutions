class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        lower = ""

        for c in s :
            if ord(c) >= 65 and ord(c) <= 90:
                lower += chr(ord(c) + 32 )
            else :
                lower += c
        
        return lower

        