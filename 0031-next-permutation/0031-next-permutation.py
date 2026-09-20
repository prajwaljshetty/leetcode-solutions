class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        
        pivot = -1

        for i in range(len(nums) - 2 , -1 , -1) :
            if nums[i] < nums[i + 1] :
                pivot = i
                break

        if pivot == -1 : 
            print(len(nums)//2)
            for i in range(len(nums)// 2) : nums[i] , nums[~i] = nums[~i],nums[i]
            return
        
        for i in range(len(nums) - 1 , pivot , -1) :
            if nums[i] > nums[pivot] : 
                nums[pivot] , nums[i] = nums[i] , nums[pivot]
                break
        
        left , right = pivot + 1 , len(nums) - 1

        while left < right :
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1