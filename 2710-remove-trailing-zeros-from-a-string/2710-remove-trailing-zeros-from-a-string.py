class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        length = len(num) - 1

        while num[length] == '0':
            length -= 1
        
        return num[: length + 1 ]