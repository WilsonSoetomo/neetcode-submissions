class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        maxfreq = 0
        for r in range(0, len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # important due to 0 instance
            maxfreq = max(maxfreq, count[s[r]])

            while(r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
                
