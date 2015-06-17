# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 is None:return l2
        elif l2 is None: return l1
        elif l1 is None and l2 is None: return None
        t1 = l1
        t2 = l2
        result_head = ListNode(0)
        c = result_head
        while (t1 is not None) and (t2 is not None):
            if t1.val > t2.val:
                c.next = ListNode(t2.val)
                c = c.next
                t2 = t2.next
            elif t1.val < t2.val:
                c.next = ListNode(t1.val)
                c = c.next
                t1 = t1.next
            else:
                c.next = ListNode(t1.val)
                c = c.next
                c.next = ListNode(t1.val)
                c = c.next
                t1 = t1.next
                t2 = t2.next
        if (t1 is None) and (t2 is not None):
            c.next = t2
        elif (t2 is None) and (t1 is not None):
            c.next = t1
        return result_head.next
