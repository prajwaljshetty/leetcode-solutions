class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1) :
            power = i * i
            if power == num : return True
            if power > num : return False