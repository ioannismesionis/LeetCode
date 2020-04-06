# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Example:
# Input: [2,2,1]
# Output: 1

# Input: [4,1,2,1,2]
# Output: 4


class Solution:
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                break
        return num


solution = Solution()
print("The single number is:", solution.singleNumber([4, 1, 2, 1, 2]))
