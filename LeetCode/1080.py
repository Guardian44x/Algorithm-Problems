"""
$1080. Insufficient Nodes in Root to Leaf Paths
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        def dfs(root, sum_val):
            root.sum = root.val + sum_val
            if root.left == None and root.right == None:
                return False if root.sum < limit else True
            lflag, rflag = False, False
            if root.left != None:
                lflag = dfs(root.left, root.sum)
                if not lflag:
                    root.left = None
            if root.right != None:
                rflag = dfs(root.right, root.sum)
                if not rflag:
                    root.right = None
            if not lflag and not rflag:
                return False
            return True
        return root if dfs(root, 0) else None