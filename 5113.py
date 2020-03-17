'''
$5113. Remove Interval
'''

class Solution:
    def removeInterval(self, intervals, toBeRemoved):
        res = []
        for interval in intervals:
            if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
                res.append(interval)
                continue
            if interval[0] >= toBeRemoved[0] and interval[1] <= toBeRemoved[1]:
                continue
            if interval[0] <= toBeRemoved[0] and interval[1] >= toBeRemoved[1]:
                if not interval[0] == toBeRemoved[0]:
                    res.append([interval[0], toBeRemoved[0]])
                if not interval[1] == toBeRemoved[1]:
                    res.append([toBeRemoved[1], interval[1]])
                continue
            if interval[0] <= toBeRemoved[0]:
                left, right = interval[0], toBeRemoved[0]
            else:
                left, right = toBeRemoved[1], interval[1]
            res.append([left, right])
        print(res)
        new_res = []
        for interval in res:
            if new_res != []:
                prev = new_res[-1]
                if interval[0] >= prev[1]:
                    new_res.append(interval)
                elif interval[1] <= prev[1]:
                    continue
                else:
                    new_res.pop()
                    new_res.append([prev[0], interval[1]])
            else:
                new_res.append(interval)
        return new_res

sol = Solution()
intervals = [[0, 100]]
toBeRemoved = [0, 50]
print(sol.removeInterval(intervals, toBeRemoved))


            
            