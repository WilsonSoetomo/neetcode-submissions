class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = sorted(stones, reverse=True)
        while len(res) > 1:
            largest = res.pop(0)
            if len(res) < 2:
                return largest - res.pop(0)
            lessLarge = res.pop(0)
            res.append(largest-lessLarge)
            res.sort(reverse=True)
        
        return res[0]

