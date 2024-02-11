# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0, 1, 2, 4, 5, 6, 7] might become[4, 5, 6, 7, 0, 1, 2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# Output: -1


class Solution:
    def binary_search(self, nums, left, right, target):
        # if we can still split
        # split and apply binary search
        if right >= left:
            # split the array to half
            idx = left + (right - left) // 2

            if nums[idx] == target:
                return idx
            elif (target < nums[idx]):
                return self.binary_search(nums, left, idx - 1, target)
            else:
                return self.binary_search(nums, idx + 1, right, target)
        # else we did not find the value
        else:
            return -1

    def split_point(self, nums, left, right):
        # base cases
        if right < left:
            return -1
        if right == left:
            return right

        # take the mid of the list provided
        split = int((left + right)/2)

        if (split < right) and (nums[split] > nums[split + 1]):
            return split
        if (split > left) and (nums[split] < nums[split - 1]):
            return (split - 1)
        if nums[left] >= nums[split]:
            return self.split_point(nums, left, split - 1)

        return self.split_point(nums, split + 1, right)

    def search(self, nums, target):
        # base case
        if len(nums) == 0:
            return -1

        # we search for the split point in our array
        # if exists
        split = self.split_point(nums, 0, len(nums) - 1)

        # if we did not find any, then array is sorted
        # we just apply binary search
        if split == -1:
            idx = self.binary_search(nums, 0, len(nums) - 1, target)

        # if the split point is our targer, return this index
        elif nums[split] == target:
            return split

        # if the beginning of the array is smaller than our target,
        # then the answer lies on the left-hand side (due to sorted)
        elif (nums[0] <= target):
            idx = self.binary_search(nums, 0, split - 1, target)
        # else it is on the other side of the split
        else:
            idx = self.binary_search(nums, split + 1, len(nums) - 1, target)

        return idx


# Example to use:
nums = [1, 3, 5]
target = 3

solution = Solution()
print("Number {target} is present at index {index}:".format(
    target=target, index=solution.search(nums, target)))
