class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapCount = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            mapCount[i] = 1 + mapCount.get(i,0)
        for n, c in mapCount.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
                