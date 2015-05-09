# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if (p and (not q)) or (q and (not p)):
            return False
        elif (not p) and (not q):
            return True
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)