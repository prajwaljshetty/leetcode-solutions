class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count = 0

        while sum(nums) > 0 :
            minNum = float("inf")

            for i in range(len(nums)) :
                if minNum > nums[i] and nums[i] != 0 :
                    minNum = nums[i]

            for i in range(len(nums)) :
                if nums[i]: 
                    nums[i] -= minNum
            count += 1
            
        
        return count
        