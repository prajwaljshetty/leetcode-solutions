class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        
        def gcd( a, b ):
            if b == 0 : return a
            return gcd( b , a % b)
    
        kinds = defaultdict(int)

        for card in deck :
            kinds[card] += 1
        
        x = 0 

        for card in kinds :
            x = gcd( kinds[card] , x)
        
        return x > 1