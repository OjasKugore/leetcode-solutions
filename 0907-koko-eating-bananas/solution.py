import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(piles: List[int], k: int, h: int) -> bool:
            total = 0
            for pile in piles:
                total += math.ceil(pile/k)
            if total <= h:
                return True
            return False
        
        low = 1
        high = max(piles)
        while (low<high):
            mid = low + (high - low)//2
            if check(piles, mid, h):
                high = mid
            else:
                low = mid + 1
        return low

