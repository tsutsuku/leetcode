# Definition for a binary tree node.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):


def binaryTreeBuild(tree):
    """
    :type tree: list[int]
    :return: TreeNode
    """
    return treeBuild(0, TreeLinkNode(None), tree)


def treeBuild(index, root, tree):
    root.val = tree[index]
    if index < len(tree) / 2 - 1:
        root.left = treeBuild(index * 2 + 1, TreeLinkNode(None), tree)
        root.right = treeBuild(index * 2 + 2, TreeLinkNode(None), tree)
    return root


tree = [1, 2, 3, 4, 5, 6, 7]

print(Solution().connect(binaryTreeBuild(tree)))
