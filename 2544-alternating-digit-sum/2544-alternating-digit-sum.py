class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digitSum = 0
        polar = len(str(n)) % 2

        while n > 0 :
            digit = n % 10
            digitSum = digitSum + (digit if polar else -digit)
            n , polar = n//10 , not polar
        
        return digitSum