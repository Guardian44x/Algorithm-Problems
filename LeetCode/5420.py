
"""
$5420. Final Prices With a Special Discount in a Shop
"""

class Solution:
    def finalPrices(self, prices):
        l = len(prices)
        moneys = [0] * l
        stacks = []
        for i in range(l-1, -1, -1):
            c = prices[i]
            while len(stacks) > 0 and stacks[-1] > c:
                stacks.pop()
            moneys[i] = prices[i] - stacks[-1] if len(stacks) > 0 else prices[i]
            stacks.append(c)
        return moneys
