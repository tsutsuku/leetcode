# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        list = []
        if root != None:
            self.level(root, 0, list)
        return list

    def level(self, root, deep, list):
        if len(list) == deep:
            list.append([])
        if root.val != None:
            list[deep].append(root.val)
        if root.left != None:
            self.level(root.left, deep + 1, list)
        if root.right != None:
            self.level(root.right, deep + 1, list)


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
root = [1, 2, 3, None, None, 15, 7]
print(Solution().levelOrder(binaryTreeBuild(root)))
