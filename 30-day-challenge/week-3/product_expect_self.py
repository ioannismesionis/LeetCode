# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint:
# It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity?
# (The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution:
    def left_cumprod(self, nums):
        prod = 1
        left = []
        for i in range(len(nums)):
            left.append(prod)
            # omit self from multiplying
            prod *= nums[i]

        return left

    def right_cumprod(self, nums):
        prod = 1
        right = []
        for i in range(len(nums) - 1, -1, -1):
            right.append(prod)
            # omit self from multiplying
            prod *= nums[i]

        right.reverse()

        return right

    def productExceptSelf(self, nums):
        left = self.left_cumprod(nums)
        right = self.right_cumprod(nums)

        return [l * r for l, r in zip(left, right)]


# Example to use
nums = [1, 2, 3, 4]

solution = Solution()
print("The prod of the list excluding self is:",
      solution.productExceptSelf(nums))
