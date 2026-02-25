# Given two binary strings a and b, return their sum as a binary string.
from itertools import zip_longest
from typing import Any


class Solution:
    def addBinary(self, a: str, b: str):
        # counter = '0'
        result = ''
        # max_len = len(a)
        # if len(a) < len(b):
        #     max_len = len(b)
        #
        # for i in range(-1, -max_len, -1):
        #
        # for i,j in zip_longest(reversed(a), reversed(b), fillvalue="0"):
        #     if i == j == '1':
        #         counter = '1'
        #         result += '0'
        #     elif counter ==  i == j == '1':
        #         result += '1'
        #     elif counter == '1' and (i == '1' or j == '1'):
        #         result += '0'
        #     elif counter == '1' and i ==  j == '0':
        #         result += '1'
        #         counter = '0'
        #     elif counter == '0' and (i == '1' or j == '1'):
        #         result += '1'
        #     else:
        #         result += '0'
        res = [ i + j for i,j in
                zip_longest(reversed([int(i) for i in list(a)]),
                            reversed([int(i) for i in list(b)]), fillvalue=0)]

        count = 0
        result = []
        for num in res:
            num +=count
            count = 0
            if num == 3:
                result.append(1)
                count = 1
            elif num == 2:
                result.append(0)
                count = 1
            else:
                result.append(num)

        if count == 1:
            result.append(1)
        result.reverse()
        return "".join(map(str, result))

print(Solution().addBinary('11', '1'))