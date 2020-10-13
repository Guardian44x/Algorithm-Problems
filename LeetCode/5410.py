
"""
5410. Course Schedule IV
"""

import collections

class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        numCourses = n
        dic = {i: set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        res = []
        for q in queries:
            a, b = q
            pre = neigh[b]
            mark = set()
            while len(pre) > 0:
                news = set()
                if a in pre:
                    res.append(True)
                    break
                for c in pre:
                    if c in mark:
                        continue
                    mark.add(c)
                    news = news.union(neigh[c])
                # print(pre)
                # print(news)
                pre = news
            else:
                res.append(False)
        return res
    
sol = Solution()
n = 5
prerequisites = [[4,3],[4,1],[4,0],[3,2],[3,1],[3,0],[2,1],[2,0],[1,0]]
queries = [[0,1],[4,0],[0,2],[1,3],[0,1]]
print(sol.checkIfPrerequisite(n, prerequisites, queries))