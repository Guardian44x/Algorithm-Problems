"""
$25. Reverse Nodes in k-Group
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l = 0
        root = head
        while head != None:
            l += 1
            head = head.next
            if l >= k:
                break
        if l < k:
            return root
        pre = None
        head = root
        K = k
        while head != None and k > 0:
            aft = head.next
            head.next = pre
            pre = head
            head = aft
            k -= 1
        if head != None:
            root.next = self.reverseKGroup(head, K)
        return pre