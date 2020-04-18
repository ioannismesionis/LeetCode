# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1->3->1->1->1 minimizes the sum.


class Solution:
    def recursive_path(self, grid, i, j, visited):
        # we reached our destination
        if (i + 1 == len(grid)) and (j + 1 == len(grid[i])):
            return grid[i][j]
        # if we go out of range return maximum
        # since we return the minimum
        elif (i >= len(grid)) or (j >= len(grid[i])):
            return float('inf')

        # check if visited the current index
        if (i, j) not in visited:
            visited[(i, j)] = grid[i][j] + min(self.recursive_path(grid, i + 1,
                                                                   j, visited), self.recursive_path(grid, i, j + 1, visited))

        return visited[(i, j)]

    def minPathSum(self, grid):
        i = 0
        j = 0
        # dictionary to store previously visited places
        # if not, we get run time error
        visited = {}

        return self.recursive_path(grid, i, j, visited)


# Example to use:
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

solution = Solution()
print("The min path sum is the following", solution.minPathSum(grid))
