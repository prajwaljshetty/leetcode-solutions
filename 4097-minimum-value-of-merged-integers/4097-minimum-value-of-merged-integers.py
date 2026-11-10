class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        minMerge = float("inf")

        for i in range(0 , len(nums) - 1 , 2) :
            print((nums[i] * int('1' + ('0' * len(str(nums[i + 1]))))) + nums[i + 1])
            minMerge = min(minMerge  , ((nums[i] * int('1' + ('0' * len(str(nums[i + 1]))))) + nums[i + 1]))
        return minMerge