class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        filtered = ""

        for c in word:
            if ord(c) > 47 and ord(c) < 58 :
                filtered += c
            else:
                filtered += " "
                
        return len(set(map(int,filtered.split())))