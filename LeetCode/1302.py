"""
$1302. Deepest Leaves Sum
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        nodes = [root]
        while nodes:
            next_nodes = []
            sum_val = 0
            for node in nodes:
                sum_val += node.val
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes
        return sum_val
            