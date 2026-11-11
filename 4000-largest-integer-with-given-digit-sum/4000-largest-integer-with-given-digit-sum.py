class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        maxDigitSum = float("-inf")

        def permute(target , length , combo ) :
            nonlocal maxDigitSum
            if sum(combo) == target and len(combo) == n:
                maxDigitSum = max(maxDigitSum , sum([e * (10 ** i) for i , e in enumerate(combo)]))
            
            if len(combo) == n :
                return
            
            for digit in range(0, 10) :
                combo.append(digit)
                permute(target , length , combo)
                combo.pop()
    
        permute(s , n , [])
        return maxDigitSum if maxDigitSum >=0 else -1