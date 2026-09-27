class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = re.sub("[!?',;.]"," ",paragraph)
        words = paragraph.split()
        wordCount = { word.lower() : 0 for word in words }
        
        for word in words:
            if word.lower() not in banned:
                wordCount[word.lower()] += 1
        
        commonWord , maxCount = '' , 0

        for word , count in wordCount.items():
            if count > maxCount : 
                commonWord = word
                maxCount = count
        
        return commonWord