"""
$638. Shoppint Offers
"""

class Solution:
    def shoppingOffers(self, price, special, needs):
        d = {}
        def dfs(cur):
            val = sum(cur[i]*price[i] for i in range(len(needs))) #cost without special
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0: # skip deals that exceed needs
                    val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[-1]) # .get check the dictionary first for result, otherwise perform dfs.
            d[tuple(cur)] = val
            return val
        return dfs(needs)