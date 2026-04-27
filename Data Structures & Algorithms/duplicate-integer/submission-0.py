class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = []
        for i in nums:
            if i not in stack:
                stack.append(i)
            elif i in stack:
                return True
        return False