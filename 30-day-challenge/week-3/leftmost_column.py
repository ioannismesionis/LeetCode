# (This problem is an interactive problem.)

# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

# You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

# BinaryMatrix.get(x, y) returns the element of the matrix at index(x, y)(0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements[n, m], which means the matrix is n * m.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

# For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.


# Example 1:

# Input: mat = [[0, 0], [1, 1]]
# Output: 0
# Example 2:

# Input: mat = [[0, 0], [0, 1]]
# Output: 1
# Example 3:

# Input: mat = [[0, 0], [0, 0]]
# Output: -1
# Example 4:


# Input: mat = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
# Output: 1


# Constraints:

# 1 <= mat.length, mat[i].length <= 100
# mat[i][j] is either 0 or 1.
# mat[i] is sorted in a non-decreasing way.

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def binary_search(self, binaryMatrixRow, i, left, right, target):
        # if we can still split
        # split and apply binary search
        if right >= left:
            # split the array to half
            idx = left + (right - left) // 2
            val = binaryMatrixRow.get(i, idx)
            # in case the value is our target
            # we have to make sure it is the left-most 1
            if val == target:
                if idx == 0:
                    return idx
                elif binaryMatrixRow.get(i, idx - 1) != target:
                    return idx
                # if the value on the left of our captured 1 is 1, then continue
                # the binary search
                else:
                    return self.binary_search(binaryMatrixRow, i, left, idx - 1, target)
            elif (target < val):
                return self.binary_search(binaryMatrixRow, i, left, idx - 1, target)
            else:
                return self.binary_search(binaryMatrixRow, i, idx + 1, right, target)
        # else we did not find the value
        else:
            return -1

    def leftMostColumnWithOne(self, binaryMatrix):
        # capture the iterations that needs to be done
        rows, columns = binaryMatrix.dimensions()
        res = 101  # due to constraint 100
        for i in range(0, rows):
            # due binary search for every row
            idx = self.binary_search(binaryMatrix, i, 0, columns - 1, 1)

            # update the left-most index if 1 is captured
            if idx != -1:
                res = min(res, idx)
        # if the res didnt capture any 1's, then its value is unchanged
        # which is 101
        if res == 101:
            return -1

        return res
