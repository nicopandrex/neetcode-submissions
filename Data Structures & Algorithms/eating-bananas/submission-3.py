import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        canidate = max(piles)
        while low <= high:
            middle = (low + high) // 2
            available = h
            for pile in piles:
                available -= math.ceil(pile / middle )
            if available >= 0 :
                canidate = min(canidate, middle)
                high = middle - 1
            else:
                low = middle + 1
        return canidate






        


        

