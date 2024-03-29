# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def subtree(self, tree):
        if tree == None:
            return 0
        else:
            left = self.subtree(tree.left)
            right = self.subtree(tree.right)
            self.diameter = max(self.diameter, right + left)
        return max(left + 1, right + 1)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        if root != None:
            self.subtree(root)

        return self.diameter
