class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        rem = 0
        for i in range(len(num) - 1, -1 , -1):
            digit = (k % 10)

            if (total := (num[i] + digit)) > 9 :
                k = (k//10) + 1
            else :
                k = (k//10)

            rem = total % 10
            num[i] = rem

        if k > 0 :
            return list(map(int , list(str(k)))) + num

        
        return num