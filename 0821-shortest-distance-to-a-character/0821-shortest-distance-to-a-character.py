class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        shortest, stack = [0 for _ in range(len(s))], []
        prevE = float("-inf")

        for index, char in enumerate(s):
            if char == c:
                currIndex = index - 1

                while stack:
                    stack.pop()
                    shortest[currIndex] = min(currIndex - prevE, index - currIndex)
                    currIndex -= 1

                prevE = index
            else:
                stack.append(char)

        currIndex = len(s) - 1

        while stack:
            stack.pop()
            shortest[currIndex] = currIndex - prevE
            currIndex -= 1

        shortest[prevE] = 0

        return shortest