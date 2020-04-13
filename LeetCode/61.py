"""
$61. Rotate List
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        first = head
        second = head
        l = 0
        while first != None:
            first = first.next
            l += 1
        first = head
        k = int(k % l)
        while k > 0:
            k -= 1
            if second.next == None:
                second = head
            else:
                second = second.next
        
        while second.next!= None:
            first = first.next
            second = second.next
        
        new_head = first.next if first.next != None else head
        second.next = head
        first.next = None
        
        return new_head