import heapq
import math


T = int(input())

for t in range(T):
    N, K = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))

    times = []
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        heapq.heappush(times, [-1*diff, 0])
    
    for i in range(K):
        diff, count = heapq.heappop(times)
        diff, count = diff * (count + 1) / (count + 2), count + 1
        heapq.heappush(times, [diff, count])
    
    res, _ = heapq.heappop(times)

    print("Case #{}: {}".format(t+1, math.ceil(-1 * res)))
    