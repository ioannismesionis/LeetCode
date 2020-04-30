# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree.

# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.


# Example 1:

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation:
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
# Other valid sequences are:
# 0 -> 1 -> 1 -> 0
# 0 -> 0 -> 0


# Example 2:

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# Output: false
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

# Example 3:

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# Output: false
# Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.


# Constraints:

# 1 <= arr.length <= 5000
# 0 <= arr[i] <= 9
# Each node's value is between [0 - 9].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def existPath(self, root, arr, n, index):
        # check whether we go out of range
        if index >= n:
            return False

        # If root is None, then there must
        # not be any element in array.
        if (root == None):
            return (n == 0)

        # If this node is a leaf and matches
        # with last entry of array.
        if ((root.left == None and root.right == None) and
                (root.val == arr[index]) and (index == n - 1)):
            return True

        # If current node is equal to arr[index]
        # this means that till this level path
        # has been matched and remaining path
        # can be either in left subtree or
        # right subtree.
        return ((index < n) and (root.val == arr[index]) and
                (self.existPath(root.left, arr, n, index + 1) or
                 self.existPath(root.right, arr, n, index + 1)))

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        n = len(arr)
        index = 0
        res = self.existPath(root, arr, n, index)

        return res
