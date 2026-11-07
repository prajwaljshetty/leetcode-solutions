class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:

        for i in range(len(arr)) :
            if arr[i] == arr[int(i + (25 / 100) * (len(arr)))] :
                return arr[i]

        