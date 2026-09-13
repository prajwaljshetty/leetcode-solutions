class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def findAVG(x,y):
            neighourSum , neighourCount =  0 , 0 
            for i , j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)] :
                if ( x + i >= 0 and x + i < len(img)) and ( y + j >= 0 and y + j < len(img[0])) :
                    neighourSum += img[x + i][y + j]
                    neighourCount += 1
            return neighourSum//neighourCount

        result = [[0] * len(img[0]) for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                result[i][j] = findAVG(i,j)
        
        return result      