class Solution:
    def findMin(self, nums: list[int]) -> int:

        def minimumBS(left , right) :
            if left == right :
                return nums[left]
            
            mid = (left + right)// 2
            
            if nums[mid] < nums[right] :
                return minimumBS(left , mid)
            elif  nums[right] < nums[mid] :
                return minimumBS(mid + 1 , right)
            
            return nums[mid]

        
        return minimumBS(0 , len(nums) - 1 )