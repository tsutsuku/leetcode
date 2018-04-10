# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(inorder[0: mid], postorder[0:mid])
        root.right = self.buildTree(inorder[mid + 1:len(inorder)], postorder[mid:len(postorder)])
        return root


inorder = [1, 2]
postorder = [2, 1]

print(Solution().buildTree(inorder, postorder))
