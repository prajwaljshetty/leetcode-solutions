class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        stack = list(t)
        index = len(s) - 1
        while stack :
            if stack[~0] != s[index] : 
                stack.pop()
            else : 
                stack.pop()
                index -= 1
        return index <= -1