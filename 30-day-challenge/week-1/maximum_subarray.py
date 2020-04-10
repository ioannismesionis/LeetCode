# Given an integer array nums, find the contiguous subarray(containing at least one number)
# which has the largest sum and return its sum.

# Example:

# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.


class Solution:
    def maxSubArray(self, nums):
        # Select the first value by default since
        # LeetCode expects length larger than 1
        max_sum = [nums[0]]

        # iterate to find the best possible sum
        # for every i we have
        for i in range(1, len(nums)):
            max_sum.append(max(nums[i], nums[i] + max_sum[i - 1]))

        return max(max_sum)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print("The maximum subarray sum is:", solution.maxSubArray(nums))
