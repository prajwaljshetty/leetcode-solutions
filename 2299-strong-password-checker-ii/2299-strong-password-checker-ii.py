class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8 : 
            return False

        def ctype(character : str) -> int:
            order = ord(character)
            if order > 96 and order < 123 :
                return 0 
            elif order > 64 and order < 91 :
                return 1
            elif order > 47 and order < 58 :
                return 2
            return 3

        criteria = [False] * 4
        criteria[ctype(password[0])] = True

        for i in range(1 , len(password)) :
            if password[i] == password[i - 1] :
                return False
            criteria[ctype(password[i])] = True

        return all(criteria)