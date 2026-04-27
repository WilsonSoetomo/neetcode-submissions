class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [*s]
        t = [*t]


        return sorted(s) == sorted(t)