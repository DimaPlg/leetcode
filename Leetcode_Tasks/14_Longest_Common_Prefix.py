# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List


class CommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_str = strs[0]
        length = len(min(strs, key=len))
        for i in range(0, length):
            for str1 in strs:
                if str1[i] != common_str[i]:
                    return common_str[:i]
        return common_str[:length]

    # if length == 0:
    #     return ''
    #
    # for j in range(1, len(strs)):
    #     if length == 0:
    #         break
    #     for i in range(len(strs[j])):
    #         length = i
    #         if strs[j][i] != common_str[i]:
    #             if i == 0:
    #                 length = -1
    #             break
    # if length == 0:
    #     return common_str[0]
    # elif length == -1:
    #     return ''
    # return common_str[:length]
print(CommonPrefix().longestCommonPrefix(["ab", "a"]))
print(CommonPrefix().longestCommonPrefix(["flower","flow","flight"]))
print(CommonPrefix().longestCommonPrefix(["dog","racecar","car"]))
print(CommonPrefix().longestCommonPrefix(["flower","flower","flower","flower"]))


