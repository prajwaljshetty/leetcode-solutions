class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parentheses = []
        def build( openCount , closeCount , curr ):
            if len(curr) == ( 2 * n ) :
                parentheses.append(curr)
                return

            if openCount < n :
                build( openCount + 1 , closeCount , curr + '(')
            
            if closeCount < openCount :
                build( openCount , closeCount + 1 , curr + ')')
        
        build( 0 , 0 , "" )

        return parentheses