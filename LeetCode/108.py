# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            Node = TreeNode(nums[0])
            return Node
        m = len(nums) // 2
        Node = TreeNode(nums[m])
        left_subtree = self.sortedArrayToBST(nums[:m])
        right_subtree = self.sortedArrayToBST(nums[(m+1):])
        Node.left = left_subtree
        Node.right = right_subtree
        return Node