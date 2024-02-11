# # means a backspace character.
# Given two strings S and T, return if they are equal when both are typed into empty text editors.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?


class Solution:
    def hash_clean(self, string):
        # list for the values to keep
        keep = []
        for ind in string:
            # append the individual str if not '#'
            if ind != '#':
                keep.append(ind)
            # if the '#' is not in the beginning
            # perform the deletion by popping the last value
            elif (ind == '#') & (len(keep) != 0):
                keep.pop(-1)

        return keep

    def backspaceCompare(self, S, T):
        return self.hash_clean(S) == self.hash_clean(T)


# Examples for testing
# Answer should be 'True'
S = "ab##"
T = "c#d#"

solution = Solution()
print("The answer is:", solution.backspaceCompare(S, T))
