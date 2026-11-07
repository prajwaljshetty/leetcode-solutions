class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numMap = {}

        for ele in nums :
            if numMap.get(ele , 0) :
                return ele
            numMap[ele] = 1
            
