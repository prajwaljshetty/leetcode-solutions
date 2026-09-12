class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False

        if len(set(pattern)) != len(set(s)):
            return False

        patternMap = {}

        for index, char in enumerate(pattern):
            if char in patternMap:
                if patternMap[char] != s[index]:
                    return False
            else:
                if s[index] in patternMap.values():
                    return False
                patternMap[char] = s[index]

        return True