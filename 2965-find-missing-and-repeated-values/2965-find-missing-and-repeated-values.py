class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        map ={}

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                    map[grid[i][j]] = map.get( grid[i][j] , 0) + 1
        
        repeated , missing = -1 , -1

        for num in range(1 , len(grid) ** 2 + 1) :
            if map.get(num , -1) == -1:
                missing = num
            elif map.get(num , -1) == 2:
                repeated = num
        
        return [repeated, missing]