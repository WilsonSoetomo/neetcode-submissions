class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])

        res = []
        res.append(intervals[0])
        
        for start, end in intervals:
            prev_end = res[-1][1]

            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])

        return res
            
            