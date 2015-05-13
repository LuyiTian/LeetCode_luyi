# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return []
        if not head.next:
            return head
        previous = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = previous
            previous = cur
            cur = tmp
        return previous
