class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        oneRowWords = []
        def checkRow( word ,  row ):
            for i in range(0,len(word)) :
                if word[i] not in row : return False
            return True

        for index , word in enumerate(words) :
            for row in ["qwertyuiop","asdfghjkl","zxcvbnm"]:
                if checkRow(word.lower(),row) : 
                    oneRowWords.append(word)
                    break

        return oneRowWords