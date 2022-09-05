# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = [0]
        lru_cache(None)
        def dfs(node):
            if(not node):
                return []
            if not(node.left or node.right):
                return [1]
            l = dfs(node.left)
            r = dfs(node.right)
            for i in l:
                for j in r:
                    if(i+j <= distance):
                        ans[0] += 1
            return [i+1 for i in l+r]

        dfs(root)
        return ans[0]