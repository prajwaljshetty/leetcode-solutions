class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1 : return False

        for i in range(0,n):
            exp = 3 ** i
            if 3 ** i == n : return True
            if exp > n : return False     