class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        seen = set()
        candidates = {}

        for a,  b in trust :
            seen.add(a)
            candidates[b] = candidates.get(b , 0) + 1
        
        if len(seen) == n : 
            return -1 
        
        for candidate in candidates :
            if candidate not in seen and candidates[candidate] == n - 1: 
                return candidate
        
        return n  if n == 1 and not trust else -1