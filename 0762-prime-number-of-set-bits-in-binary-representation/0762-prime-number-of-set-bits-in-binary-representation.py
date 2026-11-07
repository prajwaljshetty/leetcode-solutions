class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(num : int) -> bool :
            for i in range(2 , (num // 2 )+ 1) :
                if num % i == 0 :
                    return False
            
            return num > 1

        def countSetBits(num):
            BitCount = 0
            while num > 0 :
                BitCount += 1 if (num & 1) else 0
                num >>= 1
            return BitCount
        

        count = 0

        for i in range(left,right + 1) :
            if isPrime(countSetBits(i)) :
                count += 1
        
        return count

        