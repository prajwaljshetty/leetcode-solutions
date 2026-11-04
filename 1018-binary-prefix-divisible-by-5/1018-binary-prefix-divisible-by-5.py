class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:

        isDivisible = []
        prefixSum = 0

        for i in range(len(nums)) :
            prefixSum = prefixSum * 2 + nums[i]
            isDivisible.append(prefixSum % 5 == 0)

        return isDivisible