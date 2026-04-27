class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        actual_res = []
        for word in strs:
            if str(sorted(word)) not in res:
                res[str(sorted(word))] = [word]
            else:
                res[str(sorted(word))].append(word)
        for key, listed in res.items():
            actual_res.append(listed)
        return actual_res