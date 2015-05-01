# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if not head:
            return None
        if not head.next:
            if head.val == val:
                return None
            else:
                return head
        else:
            cur_node = head
            pre_node = None
            while cur_node:
                if cur_node.val == val:
                    if not pre_node:
                        head = cur_node.next
                        cur_node = cur_node.next
                    else:
                        pre_node.next = cur_node.next
                        cur_node = cur_node.next
                else:
                    if cur_node.next:
                        pre_node = cur_node
                        cur_node = cur_node.next
                    else:
                        return head
        return head


if __name__ == '__main__':
    L = [ListNode(i) for i in [1,2,6,3,4,5,6]]
    for i in range(len(L)-1):
        L[i].next = L[i+1]
    A = Solution()
    new_L = A.removeElements(L[0], 6)
    print new_L
    tmp = new_L
    while tmp:
        print tmp.val
        tmp = tmp.next
