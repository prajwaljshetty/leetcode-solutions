class Solution:
    def guessNumber(self, n: int) -> int:
        def pick(left,right):
            if left > right : return -1
            mid  = (left + right)//2
            offset = guess(mid)
            if offset == 0 :
                return mid
            elif offset == 1 :
                return pick(mid+1,right)
            else :
                return pick(left,mid-1)
        
        return pick(0,n)