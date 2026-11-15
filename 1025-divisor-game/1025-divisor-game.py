class Solution:
    def divisorGame(self, n: int) -> bool:
        def makechoice( start , end ) :
            if start >= end :
                return -1
            
            for choice in range(start , end):
                if end % choice == 0 : 
                    return choice
        
        flag = False
        offset = 1
        while n > 0 :
            choice = makechoice(offset , n)

            if choice == -1 :
                return flag

            flag = not flag
            n -= choice
        
        return flag
        