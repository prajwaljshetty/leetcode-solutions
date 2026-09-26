class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        return ( 0 if n <= 0 else 
                n if (n == 1 or n == 2) else
                self.climbStairs(n - 1) + self.climbStairs(n - 2)
            )
        
        