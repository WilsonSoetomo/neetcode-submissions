class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, numlist):
            if sum(numlist) == target:
                res.append(numlist.copy())
                return
            elif sum(numlist) > target or index >= len(nums):
                return
            numlist.append(nums[index])
            backtrack(index, numlist)
            numlist.pop()
            backtrack(index + 1, numlist)
        backtrack(0, [])

        return res