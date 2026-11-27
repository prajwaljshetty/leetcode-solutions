class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        consumed  , travelDistance = 0 , 0

        while mainTank > 0 :
            mainTank , consumed = mainTank - 1 , consumed + 1
            if consumed == 5 and additionalTank > 0 :
                mainTank , additionalTank = mainTank + 1 , additionalTank - 1
                consumed = 0
            travelDistance += 10
        
        return travelDistance