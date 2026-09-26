class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        index = 0

        for char in t:
            if index < len(s) and char == s[index]:
                index += 1
        return index == len(s)