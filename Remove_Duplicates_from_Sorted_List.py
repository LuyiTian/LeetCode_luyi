# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return None
        cur_node = head
        while cur_node.next:
            if cur_node.next.val == cur_node.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return head


if __name__ == '__main__':
    L = [ListNode(i) for i in [1,1,2,3,3]]
    for i in range(len(L)-1):
        L[i].next = L[i+1]
    A = Solution()
    new_L = A.deleteDuplicates(L[0])
    print new_L
    tmp = new_L
    while tmp:
        print tmp.val
        tmp = tmp.next
