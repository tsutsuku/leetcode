# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        Solution().post_order(root, list)
        return list


    # Step One
    def level_order(self, root, list):
        if root == None:
            return

        self.level_order(root.left, list)
        self.level_order(root.right, list)
        list.append(root.val)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(4)
print(Solution().preorderTraversal(root))
