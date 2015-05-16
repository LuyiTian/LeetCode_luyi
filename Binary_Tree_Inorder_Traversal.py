# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        output = []
        def inorder(root, output):
            if root is None:
                return 
            inorder(root.left, output)
            output.append(root.val)
            inorder(root.right, output)
        inorder(root, output)
        return output