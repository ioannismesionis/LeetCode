# Given a 2d grid map of '1's(land) and '0's(water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


class Solution():
    def sink(self, grid, i, j):
        # Sanity check to make sure we do not
        # fall out of bounds
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[i])) or (grid[i][j] == '0'):
            return 0

        # recursively check the neighbours of i, j
        grid[i][j] = '0'
        self.sink(grid, i, j + 1)
        self.sink(grid, i, j - 1)
        self.sink(grid, i - 1, j)
        self.sink(grid, i + 1, j)

        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        # sanity check
        if len(grid) == 0:
            return 0

        # iterate and sink the islands detected
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands += self.sink(grid, i, j)

        # return the total number of islands
        return islands


# Example to use:
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]


solution = Solution()
print("The total number of islands is:", solution.numIslands(grid))
