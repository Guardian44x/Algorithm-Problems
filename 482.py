class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        l = len(S)
        stack = []
        res = ''
        prev = ''
        prev_l = 0
        for i in range(l-1, -1, -1):
            c = S[i]
            if c == '-':
                continue
            if c >= 'a' and c <= 'z':
                c = c.upper()
            prev = c + prev
            prev_l += 1
            if prev_l == K:
                if res:
                    res = '-' + res
                res = prev + res
                prev = ''
                prev_l = 0
        
        if prev:
            if res:
                res = '-' + res
            res = prev + res
        return res

A = Solution()
S = "2-5g-3-J"
K = 2
print(A.licenseKeyFormatting(S, K))