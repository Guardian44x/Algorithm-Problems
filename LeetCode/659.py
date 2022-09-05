"""
$659. Split Array into Consecutive Subsequences
"""

class Solution(object):
    def isPossible(self, nums):
        prev, prev_count = None, 0
        starts = collections.deque()
        for t, grp in itertools.groupby(nums):
            count = len(list(grp))
            if prev is not None and t - prev != 1:
                for _ in range(prev_count):
                    if prev < starts.popleft() + 2:
                        return False
                prev, prev_count = None, 0
            if prev is None or t- prev == 1:
                if count > prev_count:
                    for _ in range(count - prev_count):
                        starts.append(t)
                elif count < prev_count:
                    for _ in range(prev_count - count):
                        if t-1 < starts.popleft() + 2:
                            return False
            prev, prev_count = t, count
        return all(nums[-1] >= x+2 for x in starts)

class Solution(object):
    def isPossible(self, nums):
        count = collections.Counter(nums)
        tails = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True