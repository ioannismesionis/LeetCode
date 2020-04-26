# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: [5,7]
# Output: 4
# Example 2:

# Input: [0,1]
# Output: 0


class Solution:
    def rangeBitwiseAnd(self, m, n):
        res = m
        for i in range(m + 1, n + 1):
            # Given an integer n => n & 2 * n always yields 0
            if i*2 <= n:
                return 0

            res &= i
            if res == 0:
                return 0

        return res


# Example to use
m, n = [5, 7]

solution = Solution()
print("The bitwise and result is:", solution.rangeBitwiseAnd(m, n))
