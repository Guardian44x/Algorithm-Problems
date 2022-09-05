class Solution:
    def makesquare(self, matchsticks):
        perimeter = sum(matchsticks)
        match_cnt = len(matchsticks)
        if perimeter % 4 != 0 or len(matchsticks) < 4:
            return False
        edge_length = perimeter / 4
        print(matchsticks)

        def allocateMatch(edges, idx):
            print(edges, idx)
            if idx > match_cnt:
                return False
            elif idx == match_cnt:
                if edges[0] == edges[1] and edges[0] == edges[2] and edges[0] == edges[3]:
                    return True
                else:
                    return False
            if max(edges) > edge_length:
                return False
            return allocateMatch([edges[0]+matchsticks[idx], edges[1], edges[2], edges[3]], idx+1) or \
                allocateMatch([edges[0], edges[1]+matchsticks[idx], edges[2], edges[3]], idx+1) or \
                allocateMatch([edges[0], edges[1], edges[2]+matchsticks[idx], edges[3]], idx+1) or \
                allocateMatch([edges[0], edges[1], edges[2], edges[3]+matchsticks[idx]], idx+1)
        
        return allocateMatch([0, 0, 0, 0], 0)

print("hello world")
sol = Solution()
matchsticks = [1, 1, 2, 2, 2]
print(matchsticks)
res = sol.makesquare(matchsticks)
print(res)


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        value = sum(matchsticks)
        if value < 4:
            return False
        if value % 4 != 0:
            return False
        edge = value // 4
        matchsticks.sort(reverse=True)
        @cache
        def findedges(l1, l2, l3, l4, i):
            nonlocal edge
            if l1 == l2 == l3 == l4 == edge:
                return True
            if i > len(matchsticks) - 1:
                return False
            if l1 > edge or l2 > edge or l3 > edge or l4 > edge:
                return False
            return findedges(l1 + matchsticks[i], l2, l3, l4, i + 1) or findedges(l1, l2 + matchsticks[i] , l3, l4, i + 1) or findedges(l1, l2, l3 + matchsticks[i], l4, i + 1) or findedges(l1, l2, l3, l4 + matchsticks[i] , i + 1)
        return findedges(0, 0, 0, 0, 0)


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
            if res:
                return True
            edges[i] -= nums[pos]
        return res
        
