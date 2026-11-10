class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)) :
            if leftSum == (total - nums[i]) : 
                return i
            leftSum += nums[i]
            total -= nums[i]

        return -1        