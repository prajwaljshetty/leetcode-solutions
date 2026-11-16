class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = 0 
        for index , height in enumerate(sorted(heights)) :
            if heights[index] != height : 
                count += 1
        
        return count