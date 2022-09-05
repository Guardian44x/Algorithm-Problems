
class Solution:
    def reconstructQueue(self, people):
        k_array = [[] for _ in range(len(people))]
        for p in people:
            k_array[p[1]].append(p)
        res = [_ for _ in k_array[0]]
        res.sort()
        for arr in k_array[1:]:
            if len(arr) > 0:
                arr.sort(reverse=True)
                for p in arr:
                    cnt = 0
                    idx = len(res)
                    for i, r in enumerate(res):
                        if r[0] >= p[0]:
                            cnt += 1
                        if cnt == p[1]:
                            idx = i + 1
                            print(res, p, idx)
                            break
                    res.insert(idx, p)
                    print(idx, p, res)
        return res

sol = Solution()
# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
res = sol.reconstructQueue(people)
print(res)