# You are given a string s consisting only of the characters '0' and '1'. In one operation,
# you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal.
# For example, the string "010" is alternating, while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.
from idlelib.tree import TreeNode


class MinimumChangesToMakeAlternating_Binary_String:
    def minOperations(self, s: str) -> int:
        line_from_one = 0
        line_from_zero = 0
        for i in range(len(s)):
            now_element = '0' if i%2 == 0 else '1'
            if s[i] != now_element:
                line_from_zero += 1
            else:
                line_from_one += 1
        return line_from_one if line_from_one < line_from_zero else line_from_zero



print(MinimumChangesToMakeAlternating_Binary_String().minOperations("10010100"))