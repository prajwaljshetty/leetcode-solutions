class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        offset = 0
        for word in words :

                for i in range(len(word)) :
                    if i + offset >= len(s) or s[i + offset] != word[i] :
                        return False
                offset += len(word)

                if offset == len(s) : 
                    return True
                
        return offset == len(s)