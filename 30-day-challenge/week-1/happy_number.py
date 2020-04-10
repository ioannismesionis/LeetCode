# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
# (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


class Solution:
    def loop(self, n, hash_table):
        # take the sum of the squares of the digits of n
        sq = sum(map(lambda x: int(x) ** 2, str(n)))

        # if the sq = 1, then it is a happy number
        if sq == 1:
            return True
        # if sq in hash_table, then we fall into a loop -> not a happy number
        elif sq in hash_table:
            return False
        else:
            # append the sq to hash_table and continue breaking down
            hash_table.append(sq)

    def isHappy(self, n):
        hash_table = []
        res = self.loop(n, hash_table)
        # if res equals true, then happy number
        # else not a happy number
        if res:
            return True
        else:
            return False

        # return the final result
        return self.isHappy(n)


n = 19
solution = Solution()
print("Is", n, "a happy number?", solution.isHappy(n))
