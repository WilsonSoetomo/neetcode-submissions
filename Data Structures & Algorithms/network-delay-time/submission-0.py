class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build adjecency list
        edges = collections.defaultdict(list)
        for s, e, c in times:
            edges[s].append((e,c))

        visit = set()
        t = 0
        minheap = [(0, k)]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w2 + w1, n2))
                
        return t if len(visit) == n else -1