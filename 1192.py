"""
$1192. Critical Connections in a Network.
"""

from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        dic = defaultdict([])
        for c in connections:
            u, v = dic
            dic[u].append(v)
            dic[v].append(u)
        
        timer = 0
        depth, lowest, parent, visited = \
            [float("inf")]*n, [float("inf")]*n, [float("inf")]*n, [False]*n
        res = []
        
        def find(u):

            visited[u] = True
            nonlocal timer
            depth[u], lowest[u] = timer, timer
            timer += 1

            for v in dic[u]:
                if not visited[v]:
                    parent[v] = u
                    find(v)
                    if lowest(v) > lowest(u):
                        res.append([u, v])
                
                if parent[v] != [u]:
                    lowest[u] = min(lowest[u], lowest[v])
            
        find(0)
        return res
                