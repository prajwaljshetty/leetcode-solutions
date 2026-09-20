class Solution:
    def reverse(self, x: int) -> int:
        temp , reverse = x , 0

        if temp < 0 : temp = 0 - temp

        while temp > 0 :
            reverse = ( reverse * 10 ) + ( temp % 10 )
            temp //= 10
        
        return 0 if reverse.bit_length() >= 32 else ( reverse if x > 0 else 0 - reverse )