# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        Solution().pre_order(root, list)
        return list

    # Step One
    # def pre_order(self, root, list):
    #     if root != None:
    #         list.append(root.val)
    #         if root.left != None:
    #             self.pre_order(root.left, list)
    #         if root.right != None:
    #             self.pre_order(root.right, list)

    # Step Two
    # def pre_order(self, root, list):
    #     if root == None:
    #         return
    #
    #     list.append(root.val)
    #     self.pre_order(root.left, list)
    #     self.pre_order(root.right, list)

root = TreeNode(None)
# root.left = TreeNode(3)
# root.right = TreeNode(4)
print(Solution().preorderTraversal(root))
