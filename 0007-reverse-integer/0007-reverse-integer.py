class Solution:
    def reverse(self, x: int) -> int:
        temp , reverse = x , 0

        if temp < 0 : temp = -temp

        while temp > 0 :
            reverse = ( reverse * 10 ) + ( temp % 10 )
            temp //= 10
        
        return 0 if reverse > 2**31 - 1 else ( reverse if x > 0 else -reverse )