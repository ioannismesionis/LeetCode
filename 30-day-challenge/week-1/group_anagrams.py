# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#     ["ate", "eat", "tea"],
#     ["nat", "tan"],
#     ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        # defaultdict creates automatically a key
        # if the key is not present
        res = defaultdict(list)

        # iterate the individual strs
        for indv in strs:
            # create the key as a tuple of
            # unique letters in a word
            key = tuple(sorted(indv))
            res[key].append(indv)

        return res.values()


test = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print("The result is:", solution.groupAnagrams(test))
