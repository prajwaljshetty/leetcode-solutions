class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:

        isMaxima , isMinima = [] , []

        current , previous = head , None

        while current :
            isMaxima.append(False)
            isMinima.append(False)

            if current.next and previous :
                if current.val > previous.val and current.val > current.next.val :
                    isMaxima[~0] = True
                
                if current.val < previous.val and current.val < current.next.val :
                    isMinima[~0] = True
                
            previous = current
            current = current.next
        
        criticalPoints = []

        for i in range(len(isMaxima)):
            if isMaxima[i] or isMinima[i]:
                criticalPoints.append(i)
        
        if len(criticalPoints) < 2 :
            return [-1 , -1]
        
        minDistance = float('inf')

        for i in range(1, len(criticalPoints)):
            distance = criticalPoints[i] - criticalPoints[i - 1]
            
            if minDistance > distance :
                minDistance = distance
        
        maxDistance = criticalPoints[~0] - criticalPoints[0]
        
        return [minDistance , maxDistance]        