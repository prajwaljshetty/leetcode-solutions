class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        people , flag  = 1 , True

        while time > 0 :
            people += (1 if flag else -1)
            flag = not flag if people == 1 or people == n else flag
            time -= 1
        
        return people