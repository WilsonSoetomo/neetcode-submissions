import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            divisor = (low + high) // 2
            if self.count_pile(piles, divisor) <= h:
                res = divisor
                high = divisor - 1
            else:
                low = divisor + 1
        return res


    def count_pile(self, piles, divisor):
        counter = 0
        for pile in piles:
            counter += math.ceil(float(pile) / divisor)
        return counter