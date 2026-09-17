class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        existenceMap , intersection = { key : True for key in nums1 } , []
        for e in nums2 :
            if existenceMap.get(e,False) and e not in intersection :
                intersection.append(e)
        return intersection