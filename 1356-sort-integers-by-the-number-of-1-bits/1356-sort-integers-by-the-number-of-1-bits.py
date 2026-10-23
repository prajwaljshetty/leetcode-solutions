class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:

        def countBits( num ) :
            count = 0
            while num > 0 :
                if num & 1:
                    count += 1
                num >>= 1
            return count
        
        bitMap = { ele : countBits(ele) for ele in arr }

        return sorted( arr , key = lambda ele : ( bitMap[ele] , ele ) )