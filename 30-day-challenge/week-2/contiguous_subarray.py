# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.


class Solution:
    def findMaxLength(self, nums):
        cur_max = 0
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length+1):
                # examine the current sub-array
                tmp = nums[i:j]

                # we length of the sub-array must be
                # 1) twice the sum of the sub-array (due to the 0 and one principle)
                # 2) if we have more 1's, then this will be our new sub-array
                if (len(tmp) == 2*sum(tmp)) & (cur_max < sum(tmp)):
                    cur_max = sum(tmp)
                    i_idx = i
                    j_idx = j

        return len(nums[i_idx:j_idx])


# Example
nums = [0, 1, 1]
nums = [0, 0, 1, 0, 0, 0, 1, 1]

solution = Solution()
print("this is the funny length:", solution.findMaxLength(nums))
