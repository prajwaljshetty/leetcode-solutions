class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        
        for i in range(len(wordList)) :
            charList = list(wordList[i])
            for j in range(len(charList)//2):
                charList[j] , charList[len(charList) - j - 1] = charList[len(charList) - j - 1] , charList[j]
            wordList[i] = "".join(charList)

        return " ".join(wordList)