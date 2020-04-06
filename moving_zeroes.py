# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pre-specify the number of total changes that
        # need to be done
        total_changes = nums.count(0)
        changes = 0

        # i: index of list to iterrate
        i = 0

        # While the changes does are smaller than the total changes that need
        # to be dones, continue iterrating our list
        while changes < total_changes:
            if nums[i] == 0:
                # if the number is zero
                # append it to the end of the list
                nums.append(nums.pop(i))

                # update the number of changes
                changes += 1

                # continue with the same index due to .pop method
                continue
            i += 1
        return nums


nums = [0, 1, 0, 3, 12]
solution = Solution()
print("The output is", solution.moveZeroes(nums))
