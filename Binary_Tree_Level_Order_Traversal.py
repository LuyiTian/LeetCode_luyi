# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        result = {}
        if not root:
            return []

        def sublv(node, result, level):
            result.setdefault(level, []).append(node.val)
            if node.left:
                sublv(node.left, result, level+1)
            if node.right:
                sublv(node.right, result, level+1)
            if node.left is None and node.right is None:
                return None
        sublv(root, result, 0)
        return [result[i] for i in range(len(result))]
