"""
$1201. Ugly Number III
"""

class Solution:
    def nthUglyNumber(self, n, a, b, c):
        # basic function for LCM
        import math
        def lcm(x, y):
            return (x * y) // math.gcd(x, y)

        lcm1 = lcm(a, b)
        lcm2 = lcm(b, c)
        lcm3 = lcm(c, a)
        lcm4 = lcm(lcm1, lcm2)

        # count how many ugly numbers exist below x
        def count_below(x):
            return x // a + x // b + x // c + x // lcm4 - (x // lcm1 + x // lcm2 + x // lcm3)

        # binary search
        lb = 0
        ub = 2 * 10 ** 9
        while (ub - lb > 1):
            mid = (lb + ub) // 2
            if count_below(mid) >= n:
                ub = mid
            else:
                lb = mid

        return ub

        
sol = Solution()
n = 1000000000
a, b, c = 2, 217983653, 336916467
print(sol.nthUglyNumber(n, a, b, c))