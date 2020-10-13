"""
$1578. Minumum Deletion Cost to Avoid Repeating Letters
"""

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        char = ''
        char_cost = 0
        char_sum = 0
        count = 0
        res = 0
        for c, cost_i in zip(s, cost):
            if c == char:
                count += 1
                char_cost = max(cost_i, char_cost)
                char_sum += cost_i
            else:
                if count > 1:
                    res += char_sum - char_cost
                char = c
                count = 1
                char_cost = cost_i
                char_sum = cost_i
        if count > 1:
            res += char_sum - char_cost
        return res
