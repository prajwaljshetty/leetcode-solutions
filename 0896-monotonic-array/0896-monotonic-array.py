class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        x = 1
        while x < len(nums) and nums[0] == nums[x]: 
            x+= 1
        
        if x == len(nums) : return True

        if nums[0] < nums[x] :
            for i in range(1, len(nums)) :
                if nums[i] < nums[i - 1] : 
                    return False
        else :
            for i in range(1, len(nums)) :
                if nums[i] > nums[i - 1] : 
                    return False
        return True
            


        