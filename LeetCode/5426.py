
"""
5426. Reorder Routes to Make All Paths Lead to the City Zero
"""

import collections

class Solution:
    def minReorder(self, n, connections):
        starts = collections.defaultdict(set)
        ends = collections.defaultdict(set)
        for s, e in connections:
            ends[e].add(s)
            starts[s].add(e)
        count = len(starts[0])
        pres = starts[0].union(ends[0])
        mark = set([0])
        while len(pres) > 0:
            news = set()
            print(count, pres)
            for c in pres:
                mark.add(c)
                news = news.union(starts[c])
            news = news.difference(mark)
            count += len(news)
            for c in pres:
                news = news.union(ends[c])
            news = news.difference(mark)
            pres = news
        return count

sol = Solution()
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(sol.minReorder(n, connections))