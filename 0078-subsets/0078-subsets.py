class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numSet = [[]]

        for i in range(len(nums)):
            tempSet = []
            for sub in numSet:
                tempSet.append( sub + [ nums[i] ])
            numSet.extend(tempSet)
        return numSet