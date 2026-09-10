class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def fillRowAndColumns( x : int , y : int ) -> None :
            # My Two Marker Algo
            # I came up with this approach using two directional markers:
            # inf -> horizontal, -inf -> vertical.
            i , j = x - 1 , y
            while i >= 0 and matrix[i][j] != float("-inf"): matrix[i][j] , i = float("-inf") , i - 1
            i , j = x , y - 1
            while j >= 0 and matrix[i][j] != float("inf"): matrix[i][j] , j = float("inf") , j - 1

            i , j = x + 1 , y
            while i < len(matrix) and matrix[i][j] != 0 : matrix[i][j] , i = float("-inf") , i + 1
            i , j = x , y + 1
            while j < len(matrix[0]) and matrix[i][j] != 0: matrix[i][j] , j = float("inf") , j + 1

        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    matrix[i][j] = float("inf")
                    fillRowAndColumns(i,j)
        
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == float("inf") or matrix[i][j] == float("-inf") : matrix[i][j] = 0  