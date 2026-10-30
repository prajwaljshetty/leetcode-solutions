class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")

        sorted = [0] * len(words)

        for i in range(len(words)):
            j = int(words[i][~0]) - 1
            sorted[j] = words[i][:~0]
            
        return " ".join(sorted)