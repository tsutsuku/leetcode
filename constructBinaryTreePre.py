# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        root_val = preorder[0]
        preorder.remove(root_val)
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(preorder[0:mid], inorder[0: mid])
        root.right = self.buildTree(preorder[mid:len(preorder)], inorder[mid + 1:len(inorder)])
        return root


inorder = [1, 2]
preorder = [2, 1]

print(Solution().buildTree(preorder, inorder))
