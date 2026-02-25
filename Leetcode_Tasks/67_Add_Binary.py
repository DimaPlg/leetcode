# Given two binary strings a and b, return their sum as a binary string.
from itertools import zip_longest
from typing import Any


class Solution:
    def addBinary(self, a: str, b: str):
        res = [ i + j for i,j in
                zip_longest(reversed([int(i) for i in list(a)]),
                            reversed([int(i) for i in list(b)]), fillvalue=0)]

        count = 0
        result = []
        for num in res:
            num +=count
            count = 0
            if num > 1:
                result.append(num - 2)
                count = 1
            else:
                result.append(num)

        if count == 1:
            result.append(1)
        result.reverse()
        return "".join(map(str, result))

    def addBinaryV2(self, a: str, b: str):
        return bin((int(a, 2) + int(b, 2)))[2:]

    def addBinaryV3(self, a: str, b: str):
        count = 0
        res = [i + "" + j for i, j in
               zip_longest(reversed(a),reversed(b), fillvalue='0')]
        result = ''
        for element in res:
            if count == 1 and element in('01', '10'):
                result += '0'
                count = 1
            elif count == 1 and element in ('11', '00'):
                result += '1'
                count = 0
                if element == '11':
                    count = 1
            elif count == 0 and element in ('10', '01'):
                result += '1'
            elif count == 0 and element == '11':
                result += '0'
                count = 1
            else:
                result += '0'

        if count == 1:
            result += '1'
        return result[::-1]

    def addBinaryV4(self, a: str, b: str):
        count = 0
        result =''
        for i,j in zip_longest(reversed(a),reversed(b), fillvalue='0'):
            if count == 1:
                if i == j == '1':
                    result += '1'
                    count = 1
                elif i == '1' or j == '1':
                    result += '0'
                    count = 1
                else:
                    result += '1'
                    count = 0
            else:
                if i == j == '1':
                    result += '0'
                    count = 1
                elif i == '1' or j == '1':
                    result += '1'
                else:
                    result += '0'
        if count == 1:
            result += '1'
        return result[::-1]
# print(Solution().addBinary('11', '1'))
# print(Solution().addBinaryV3('1010', '1010'))
print(Solution().addBinaryV4('1', '111'))