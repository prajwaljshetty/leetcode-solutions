class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        frequency = {}
        maxFreq , count = float("-inf") , 0

        for item in nums :
            frequency[item] = frequency.get(item , 0) + 1 

        for item in nums :
            if frequency[item] > maxFreq :
                maxFreq , count = frequency[item] , 1
            elif frequency[item] == maxFreq :
                count += 1
        
        return count  