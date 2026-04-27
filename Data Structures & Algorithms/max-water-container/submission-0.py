class Solution:
    def maxArea(self, heights: List[int]) -> int:
        finalArea = 0
        for l, h in enumerate(heights):
            r = len(heights) - 1
            while l < r:
                area = min(h, heights[r]) * (r - l)
                finalArea = max(finalArea, area)
                r -= 1
        return finalArea

