class Solution:
    def digitSum(self, s: str, k: int) -> str:

        i = 0
        while len(s) > k:
            total = ""
            i = 0
            while i < len(s) :
                total += str(sum( map( int , s[i:i+k])))
                print(total)
                i += k
            s = total
        
        return s