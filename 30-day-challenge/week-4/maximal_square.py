# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4


class Solution:
    def maximalSquare(self, matrix):
        # base case initilisation
        rows = len(matrix)
        if rows > 0:
            cols = len(matrix[0])
        else:
            cols = 0

        # creates a list to store the square lenghts for i, j
        w, h = cols + 1, rows + 1
        dp = [[0 for x in range(w)] for y in range(h)]
        maxsqlen = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1]
                                       [j]), dp[i - 1][j - 1]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])

        return maxsqlen * maxsqlen


# Example to use:
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "0"],
          ["1", "1", "1", "1", "0"], ["1", "0", "0", "1", "0"]]

solution = Solution()
print("The maximum area is:", solution.maximalSquare(matrix))
