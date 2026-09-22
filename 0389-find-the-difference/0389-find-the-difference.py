class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        uniqueChar = 0
        for char in s + t :
            uniqueChar ^= ord(char)
        return chr(uniqueChar)