class Solution(object):
    def scoreOfParentheses(self, s):
        
        def r(start, end):
            if start + 1 == end:
                return 1

            balance = 0

            for i in range(start, end + 1):
                if s[i] == '(':
                    balance += 1
                else:
                    balance -= 1

                if balance == 0:
                    if i == end:
                        # (A)
                        return 2 * r(start + 1, end - 1)
                    else:
                        # AB
                        return r(start, i) + r(i + 1, end)

        return r(0, len(s) - 1)