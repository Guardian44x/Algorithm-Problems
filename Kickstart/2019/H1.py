"""
H-index
"""

import heapq

T = int(input())

for i in range(T):
    N = int(input())
    cites = list(map(int, input().split(' ')))

    Hidx = 0
    vals = []
    res = []

    for c in cites:
        if c <= Hidx:
            res.append(str(Hidx))
            continue
        heapq.heappush(vals, c)
        while len(vals) > Hidx and vals[0] <= Hidx:
            heapq.heappop(vals)
        if len(vals) > Hidx:
            Hidx += 1
        res.append(str(Hidx))
    
    print("Case #{}: {}".format(i+1, ' '.join(res)))