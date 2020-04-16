# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

# Example 1:
# Input: "()"
# Output: True

# Example 2:
# Input: "(*)"
# Output: True

# Example 3:
# Input: "(*))"
# Output: True

# Note:
# The string size will be in the range [1, 100].

s = '(*)'

class Solution:
    def checkValidString(self, s):
        # validity checks before engaging
        if (s == '*') | (len(s) == 0):
            return True
        if (len(s) == 1) | (s[0] == ')'):
            return False

        stack = []
        ast_stack = []
        # store the indexes of opening
        # and closing brackets
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                ast_stack.append(i)
            else:
                if len(stack) != 0:
                    stack.pop()
                elif len(ast_stack) > 0:
                    ast_stack.pop()
                else:
                    return False

        # check whether there is asterisk
        # for closing the previous bracket
        while stack and ast_stack:
            if stack[-1] - ast_stack[-1] < 0:
                stack.pop()
                ast_stack.pop()
            else:
                break

        return len(stack) == 0


# Example to use:
s = '(*)'

solution = Solution()
print("Are the brackets correctly closed?", solution.checkValidString(s))
