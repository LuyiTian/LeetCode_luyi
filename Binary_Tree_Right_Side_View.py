# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if not root:
            return []
        level_order_dict = {}
        current_level = [root]
        tmp_level = []
        level = 1
        while True:
            for node in current_level:
                if node.left:
                    tmp_level.append(node.left)
                if node.right:
                    tmp_level.append(node.right)
                level_order_dict.setdefault(level, []).append(node.val)
            if len(tmp_level) == 0:
                break
            else:
                level += 1
                current_level = tmp_level
                tmp_level = []
        level_order_tuple = level_order_dict.items()
        level_order_tuple.sort(key=lambda x: x[0])
        return [item[-1] for _, item in level_order_tuple]
