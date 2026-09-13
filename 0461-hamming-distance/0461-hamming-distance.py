class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bits  , count = x ^ y , 0
        while bits :
            count , bits = count + 1 if ( bits & 1 )else count , bits >> 1

        # (x ^ y).bit_count() bro just does everything for us
        return count