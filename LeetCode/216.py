'''
$ 216: Combination Sum III
'''

class Solution:
    def combinationSum3(self, k, n):

        def combination(k, n, sup):
            print(n, k)
            if k == 1 and n <= sup:
                return [[n]]
            if (n<(k+1)*k/2) or (k>sup) or (n>(2*sup-k+1)*k/2):
                return []
            res = []
            for p in range(min(n-k*(k-1)//2, sup), n//k, -1):
                prev = combination(k-1, n-p, p-1)
                print(prev)
                for c in prev:
                    if len(c) < k-1:
                        break
                    if p > c[0]:
                        res.append([p] + c)
            return res
        
        res = combination(k, n, 9)
        return res
            

sol = Solution()
k = 3
n = 7
print(sol.combinationSum3(k, n))