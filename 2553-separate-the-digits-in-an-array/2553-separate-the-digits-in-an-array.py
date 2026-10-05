class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        digits = []
        for i in range(len(nums) - 1 , -1 ,-1):
            while nums[i] > 0 :
                digits.append( nums[i] % 10 )
                nums[i] //= 10

        return digits[::-1]