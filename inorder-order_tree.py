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
        Solution().in_order(root, list)
        return list


    # Step One
    def in_order(self, root, list):
        if root == None:
            return

        self.in_order(root.left, list)
        self.in_order(root.right, list)
        list.append(root.val)

root = TreeNode(None)
# root.left = TreeNode(3)
# root.right = TreeNode(4)
print(Solution().preorderTraversal(root))
