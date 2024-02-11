# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

# direction can be 0 (for left shift) or 1 (for right shift).
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.


# Example 1:

# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation:
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"
# Example 2:

# Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


# Constraints:

# 1 <= s.length <= 100
# s only contains lower case English letters.
# 1 <= shift.length <= 100
# shift[i].length == 2
# 0 <= shift[i][0] <= 1
# 0 <= shift[i][1] <= 100


class Solution:
    def swift_left(self, s, count):
        return s[count:] + s[:count]

    def swift_right(self, s, count):
        l = len(s)
        return s[l-count:] + s[:l-count]

    def stringShift(self, s, shift):
        for rot in shift:
            # this is for right
            if rot[0]:
                s = self.swift_right(s, rot[1])
            # this is for left
            else:
                s = self.swift_left(s, rot[1])

        return s


# Examples to use.
s = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]


solution = Solution()
print("The outcome after the swifts is:", solution.stringShift(s, shift))

# TO-DO:
# An update could be to count the number of the left and right swifts and cancel them out
# That will essentially allows for just a single rotation with the sum of the total rotations.
