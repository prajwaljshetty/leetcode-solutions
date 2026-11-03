class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        minMap = {
            r : float("inf") 
            for r in range(len(matrix))
        }

        maxMap = {
            c : float("-inf")
            for c in range(len(matrix[0]))
        }

        for i in range(len(matrix)):
            for j in range(len(matrix[i])) :
                    minMap[i] = min(minMap[i] , matrix[i][j])
        
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                maxMap[i] = max(maxMap[i] , matrix[j][i])

        luckyNumber  = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == minMap[i] == maxMap[j]:
                    luckyNumber.append(matrix[i][j])

        return luckyNumber
        