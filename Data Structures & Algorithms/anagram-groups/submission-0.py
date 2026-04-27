class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in strs:
            sortedKey = ''.join(sorted(i))
            if sortedKey not in map:
                map[sortedKey] = []
            map[sortedKey].append(i)
        return map.values()