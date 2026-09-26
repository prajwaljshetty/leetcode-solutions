class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def inBound( a , limit ): 
            return a > -1 and a < limit 

        def isValid( x , y ) :
            return inBound( x , rows ) and inBound( y , cols ) and grid[x][y] == 1
    
        def dfs(x, y):
            if not isValid(x, y): 
                return 1
            if visited[x][y]: 
                return 0

            visited[x][y] , perimeter  = True , 0
            for i, j in [(0,-1),(-1,0),(0,1),(1,0)]: perimeter += dfs(x + i, y + j)

            return perimeter
            
        for x in range(rows) :
            for y in range(cols):
                if grid[x][y] == 1 : return dfs( x , y )
