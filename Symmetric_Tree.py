# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        def sub_sym(lsub,rsub):
            if lsub == rsub == None:
                return True
            elif lsub == None or rsub == None:
                return False
            if lsub.left == lsub.right == rsub.left == rsub.right == None:
                if lsub.val == rsub.val:
                    return True
                else:
                    return False
            else:
                if lsub.val != rsub.val: return False
                return sub_sym(lsub.right,rsub.left) and sub_sym(lsub.left,rsub.right)
        if not root:
            return True
        else:
            return sub_sym(root.left, root.right)