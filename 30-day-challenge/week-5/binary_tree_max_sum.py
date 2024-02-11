# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMax(self, root):
        # Base Case
        if root is None:
            return 0

        # l and r store maximum path sum going through left
        # and right child of root respetively
        l = self.findMax(root.left)
        r = self.findMax(root.right)

        # Max path for parent call of root. This path
        # must include at most one child of root
        max_single = max(max(l, r) + root.val, root.val)

        # Max top represents the sum when the node under
        # consideration is the root of the maxSum path and
        # no ancestor of root are there in max sum path
        max_top = max(max_single, l + r + root.val)

        # Static variable to store the changes
        # Store the maximum result
        self.res = max(self.res, max_top)

        return max_single

    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize result
        self.res = float("-inf")

        # Compute and return result
        self.findMax(root)

        return self.res
