"""
$5297. Jump Game III
"""

class Solution:
    def canReach(self, arr, start):
        l = len(arr)
        prev = set()
        nl = len(prev)
        now = [start]
        if 0 not in arr:
            return False

        while now:
            next = set()
            for s in now:
                if s-arr[s] >= 0:
                    if arr[s-arr[s]] == 0:
                        return True
                    next.add(s-arr[s])
                if s+arr[s] < l:
                    if arr[s+arr[s]] == 0:
                        return True
                    next.add(s+arr[s])
            prev = prev | next
            if len(prev) <= nl:
                return False
            else:
                nl = len(prev)
            now = next
        
sol = Solution()
arr = [3, 0, 2, 1, 2]
start = 2
res = sol.canReach(arr, start)
print(res)        