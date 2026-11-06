class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        words = sentence.split(" ")

        print(words)

        for i , word in enumerate(words) :
            if word[0] == searchWord[0]:
                index = 0
                while (index < len(searchWord) and  index < len(word)) and (searchWord[index] == word[index]):
                    index += 1
                if index == len(searchWord):
                    return i + 1
        
        return -1
        