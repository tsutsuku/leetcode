# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.checkSymmetric(root.left, root.right)

    # version 1.0
    # def checkSymmetric(self, left, right):
    #     if left == right:
    #         return True
    #     elif left != None and right != None and left.val == right.val:
    #         return True and \
    #                self.checkSymmetric(left.left, right.right) and \
    #                self.checkSymmetric(left.right, right.left)
    #     else:
    #         return False

    # Recursive
    def checkSymmetric(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False

        return self.checkSymmetric(left.left, right.right) and \
               self.checkSymmetric(left.right, right.left)

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
root = [1, 2, 3]
print(Solution().isSymmetric(binaryTreeBuild(root)))
