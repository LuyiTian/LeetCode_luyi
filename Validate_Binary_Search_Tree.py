# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
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

    def isValidBST(self, root):
        '''

        '''
        if not root:
            return True
        output = self.inorderTraversal(root)
        if False in [output[i-1]<output[i] for i in range(1,len(output))]:
            return False
        else:
            return True


if __name__ == '__main__':
    A = Solution()
    T = TreeNode(10)
    T.left = TreeNode(5)
    T.right = TreeNode(15)
    T.right.right = TreeNode(20)
    T.right.left = TreeNode(6)
    print A.isValidBST(T)
