# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2
# Note:
# The length of the array is in range[1, 20, 000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

import collections


class Solution:
    def subarraySum(self, nums, k):
        if (len(nums) == 1) and (nums[0] == k):
            return 1
        # initialize frequency sum
        freq_sum = collections.defaultdict(int)
        freq_sum[0] = 1

        rol_sum = 0  # rolling sum initilisation
        count = 0
        for i in range(len(nums)):
            # calculate the cum sum
            rol_sum += nums[i]
            if (rol_sum - k) in freq_sum:
                count += freq_sum[(rol_sum - k)]
            freq_sum[rol_sum] += 1

        return count

# Example to use:
nums = [1, 1, 1]
k = 2

solution = Solution()
print("The count is:", solution.subarraySum(nums, k))