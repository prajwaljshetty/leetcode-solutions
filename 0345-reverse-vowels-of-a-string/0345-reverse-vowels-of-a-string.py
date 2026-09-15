class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set("aeiou")
    
        left , right = 0 , len(s) - 1

        while left < right :
            leftVowel = s[left].lower() in vowels
            rightVowel = s[right].lower() in vowels
            if leftVowel and rightVowel :
                s[left] , s[right] = s[right] , s[left]
                left , right = left + 1 , right - 1
            elif leftVowel :
                right -= 1
            elif rightVowel :
                left += 1
            else :
                left , right = left + 1 , right - 1
        
        return "".join(s)