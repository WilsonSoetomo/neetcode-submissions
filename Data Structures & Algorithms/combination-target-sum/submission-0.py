class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, numList):
            if numList and sum(numList) == target:
                res.append(numList.copy())
                return
            elif numList and sum(numList) > target or index >= len(nums):
                return

            numList.append(nums[index])
            backtrack(index, numList)
            numList.pop()
            backtrack(index + 1, numList)

        backtrack(0, [])

        return res