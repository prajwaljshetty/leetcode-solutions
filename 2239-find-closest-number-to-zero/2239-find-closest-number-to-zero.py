class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        close = 0

        for i in range(1 , len(nums)) :
            if abs(nums[close]) > abs(nums[i]) :
                close = i
            elif abs(nums[close]) == abs(nums[i]) :
                close = close if nums[close] > nums[i] else i
            
        return nums[close]