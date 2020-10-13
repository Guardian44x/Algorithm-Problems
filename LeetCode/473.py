"""
$473. Matchsticks to Square.
"""

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        self.girth = sum(nums)
        self.length = self.girth // 4
        if self.length * 4 != self.girth or len(nums) < 4:
            return False
        edges = [nums[0], 0, 0, 0]
        return self.dfs(nums, edges, 1)
    
    def dfs(self, nums: List[int], edges: List[int], pos: int) -> bool:
        # print(edges, pos)
        if max(edges) > self.length:
            return False
        if pos == len(nums):
            # print(edges, pos)
            if max(edges) == self.length and min(edges) == self.length:
                return True
            else:
                return False
        res = False
        for i in range(4):
            if edges[i] + nums[pos] > self.length or  \
                edges[i] in edges[:i]:
                continue      
            edges[i] += nums[pos]
            res = res or self.dfs(nums, edges, pos+1)
            edges[i] -= nums[pos]
        return res