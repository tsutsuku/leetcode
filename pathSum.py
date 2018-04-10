# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.hasTotal(root, 0, sum)

    # version 1.0
    # def hasTotal(self, root, total, sum):
    #     if root is None:
    #         return False
    #     elif root.val + total == sum and root.left is None and root.right is None:
    #         return True
    #     else:
    #         return self.hasTotal(root.left, root.val + total, sum) or \
    #                self.hasTotal(root.right, root.val + total, sum)


def binaryTreeBuild(tree):
    """
    :type tree: list[int]
    :return: TreeNode
    """
    return treeBuild(0, TreeNode(None), tree)


def treeBuild(index, root, tree):
    root.val = tree[index]
    if index < len(tree) / 2 - 1:
        root.left = treeBuild(index * 2 + 1, TreeNode(None), tree)
        root.right = treeBuild(index * 2 + 2, TreeNode(None), tree)
    return root


# root = [3, 9, 20, None, None, 15, 7]
root = [1, 2]
print(Solution().hasPathSum(binaryTreeBuild(root), 1))
