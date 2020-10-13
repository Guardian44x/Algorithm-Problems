"""
$ Pseudo-Palindromic Paths in a Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        root.count = [0] * 10
        root.count[root.val] += 1
        root.count[root.val] %= 2
        pres = [root]
        res = 0
        while pres:
            t = pres.pop(0)
            left = t.left
            right = t.right
            if left == None and right == None:
                if sum(t.count) < 2:
                    res += 1
                continue
            if left != None:
                left.count = t.count.copy()
                left.count[left.val] += 1
                left.count[left.val] %= 2
                pres.append(left)
            if right != None:
                right.count = t.count.copy()
                right.count[right.val] += 1
                right.count[right.val] %= 2
                pres.append(right)
        return res