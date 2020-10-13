"""
$684. Redundant Connection
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [0] * len(edges)

        def find(x):
            if parents[x] == 0:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parents[rootX] = rootY
            return True

        for u, v in edges:
            if not union(u-1, v-1):
                return [u, v]
        