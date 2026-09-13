class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bits = x ^ y
        count = 0
        while bits :
            if bits & 1 : count += 1
            bits >>= 1
        return (x ^ y).bit_count()