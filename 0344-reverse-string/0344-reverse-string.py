class Solution:
    def reverseString(self, s: List[str]) -> None:
        # two pointer approach
        left , right = 0 , len(s) - 1
        mid = ( left + right ) // 2

        while left <= mid :
           s[left] , s[right] = s[right] , s[left]
           left  , right  = left + 1 , right - 1

        #for i in range(len(s)//2): s[i] , s[ len(s) - i - 1] = s[len(s) - i - 1] , s[i]

        return s