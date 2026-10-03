class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s : return 0
        stack = [-1]
        maxCount = 0
        for i in range(len(s)) :
            
            if s[i] == '(' :
                stack.append(i)
            else :
                stack.pop()
                if stack : 
                    maxCount = max(maxCount , i - stack[~0])
                else :
                    stack.append(i) 
        return maxCount