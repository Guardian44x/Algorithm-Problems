"""
$1448. Count Good Nodes in Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(root, max_val):
            nonlocal count
            if not root:
                return 
            # print(count, root.val, max_val)
            if root.val >= max_val:
                count += 1
            dfs(root.left, max(root.val, max_val))
            dfs(root.right, max(root.val, max_val))
        
        dfs(root, float("-inf"))
        return count