class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, numlist):
            if sum(numlist) == target:
                res.append(numlist.copy())
                return
            if sum(numlist) > target or index >= len(candidates):
                return

            numlist.append(candidates[index])
            backtrack(index + 1, numlist)
            numlist.pop()
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, numlist)

        backtrack(0, [])
        return res