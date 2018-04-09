# # Definition for a binary tree node.
# import math
#
#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# # version 1.0
# # class MaxDeep:
# #     def __init__(self):
# #         self.val = 0
# #
# # class Solution:
# #     def maxDepth(self, root):
# #         """
# #         :type root: TreeNode
# #         :rtype: int
# #         """
# #         maxDe = MaxDeep()
# #         self.findMaxDepth(root, 0, maxDe)
# #         return maxDe.val
# #
# #     def findMaxDepth(self, root, depth, maxDe):
# #         if root == None:
# #             return
# #         maxDe.val = max(maxDe.val, depth + 1)
# #         if root.left == None and root.right == None:
# #             return
# #
# #         self.findMaxDepth(root.left, depth + 1, maxDe)
# #         self.findMaxDepth(root.right, depth + 1, maxDe)
#
# # good solution
# class Solution:
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root == None:
#             return 0
#         maxL = self.maxDepth(root.left)
#         maxR = self.maxDepth(root.right)
#
#         if maxL > maxR:
#             return maxL + 1
#         else:
#             return maxR + 1
#
# def binaryTreeBuild(tree):
#     """
#     :type tree: list[int]
#     :return: TreeNode
#     """
#     return treeBuild(0, TreeNode(None), tree)
#
#
# def treeBuild(index, root, tree):
#     root.val = tree[index]
#     if index < len(tree) / 2 - 1:
#         root.left = treeBuild(index * 2 + 1, TreeNode(None), tree)
#         root.right = treeBuild(index * 2 + 2, TreeNode(None), tree)
#     return root
#
#
# # root = [3, 9, 20, None, None, 15, 7]
# root = [1, 2, 3, None, None, 15, 7]
# print(Solution().maxDepth(binaryTreeBuild(root)))
