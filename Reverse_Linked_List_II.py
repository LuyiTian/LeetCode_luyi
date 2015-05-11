# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if not head.next:
            return head
        if m == n:
            return head
        tmp_index = 1
        rev_start_node = None
        rev_start_next = None
        rev_end_node = None
        tmp_node = head
        previous = None
        while True:
            if tmp_index < m:
                rev_start_node = tmp_node
                rev_start_next = tmp_node.next
                previous = tmp_node.next
                tmp_node = tmp_node.next
            elif m <= tmp_index < n:
                tmp = tmp_node.next
                tmp_node.next = previous
                previous = tmp_node
                tmp_node = tmp
            elif tmp_index == n:
                tmp = tmp_node.next
                tmp_node.next = previous
                if not rev_start_node:
                    head.next = tmp
                    return tmp_node
                else:
                    rev_start_node.next = tmp_node
                    rev_start_next.next = tmp
                    return head
            tmp_index += 1


