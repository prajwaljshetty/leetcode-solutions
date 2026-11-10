class Solution:
    def isThree(self, n: int) -> bool:
        return sum(1 if ((n % k) == 0) else 0 for k in range(1 , n + 1)) == 3