# Question No.222 Count Complete Tree Nodes
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Mine Solution
        # if not root:
        #     return 0
        # else:
        #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        # Main Solution
        #     h = self.height(root)
        #     return 0 if h < 0 else (1 << h) + self.countNodes(root.left) if self.height(root.right) else (1 << h - 1) + self.height(root.left)
        #
        # def height(self, root):
        #     return root == -1 if not root else 1 + self.height(root.left)

        # Iterative Version
    #     nodes, h = 0, self.height(root)
    #     while root:
    #         if self.height(root.right) == h - 1:
    #             nodes += 1 << h
    #             root = root.right
    #         else:
    #             nodes += 1 << h - 1
    #             root = root.left
    #         h -= 1
    #     return nodes
    #
    # def height(self, root):
    #     return root == -1 if not root else 1 + self.height(root.left)

