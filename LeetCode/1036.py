"""
$1036. Escape a Large Maze
"""

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        N=10**6
        bs=set() 
        for b in blocked:
            bs.add(tuple(b))

        def bfs(p):
            q=collections.deque()
            q.append(p)
            seen=set([tuple(p)])
            while q:
                x,y=q.popleft()
                if len(seen)>19900:return 1 # outside
                for nx,ny in ((x-1,y),(x,y-1),(x,y+1),(x+1,y)):
                    if (nx,ny) not in bs and (nx,ny,) not in seen and 0<=nx<N and 0<=ny<N:
                        q.append((nx,ny))
                        seen.add((nx,ny))
            return 0 # inside

        x,y=bfs(source),bfs(target)
        if x ^ y==1:return False
        else:return True