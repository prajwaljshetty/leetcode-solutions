class Solution:
    def checkRecord(self, s: str) -> bool:
        absent , late = 0 , 0
        for c in s :
            if c == 'A' : 
                absent += 1
                if absent >= 2 : return False
                late = 0
            elif c == 'L' :
                late += 1
                if late >= 3 : return False
            else :
                late = 0
        return True

        