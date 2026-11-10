class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        minMerge = float("inf")

        for i in range(0, len(nums), 2):
            digits = len(str(nums[i + 1]))
            merged = nums[i] * (10 ** digits) + nums[i + 1]
            minMerge = min(minMerge, merged)

        return minMerge