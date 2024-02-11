# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not).
# A common subsequence of two strings is a subsequence that is common to both strings.

# If there is no common subsequence, return 0.


# Example 1:

# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.


# Constraints:

# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.


class Solution:
    def lcs(self, text1, text2, l1, l2):
        # return if already calculated
        if (l1, l2) in self.memory:
            return self.memory[(l1, l2)]

        # else proceed with the calculated
        # explore base case first
        if l1 == 0 or l2 == 0:
            return 0

        # Case 1: texts end in the same character
        elif text1[l1-1] == text2[l2-1]:
            res = 1 + self.lcs(text1, text2, l1-1, l2 - 1)
        # Case 2: do not end in the same character
        elif text1[l1-1] != text2[l2-1]:
            tmp1 = self.lcs(text1, text2, l1 - 1, l2)
            tmp2 = self.lcs(text1, text2, l1, l2 - 1)

            # take the maximum of the two
            res = max(tmp1, tmp2)
        # store the calculated result
        self.memory[(l1, l2)] = res

        return res

    def longestCommonSubsequence(self, text1, text2):
        l1 = len(text1)
        l2 = len(text2)

        # empty dict to store already calculated results
        self.memory = {}
        res = self.lcs(text1, text2, l1, l2)

        return res


# Example to use:
text1 = "abcde"
text2 = "ace"

solution = Solution()
print("The length of the longest common subsequence is:",
      solution.longestCommonSubsequence(text1, text2))
