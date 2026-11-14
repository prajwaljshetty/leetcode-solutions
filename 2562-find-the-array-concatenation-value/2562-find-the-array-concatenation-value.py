class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        value  , n = 0 , len(nums) - 1

        for i in range(0 , (n // 2)+ 1) :
            if i == n - i:
                value += nums[i]
            else:
                value += int(str(nums[i]) + str(nums[n - i]))
        
        return value