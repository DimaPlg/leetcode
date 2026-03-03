# Given two positive integers n and k, the binary string Sn is formed as follows:
#
# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation,
# reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x
# (0 changes to 1 and 1 changes to 0).
from operator import invert



class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        length = (1 << n) - 1
        mid = (length + 1) // 2

        if k == mid:
            return '1'
        if k < mid:
            return self.findKthBit(n - 1, k)

        c = self.findKthBit(n - 1, length - k + 1)
        return '1' if c == '0' else '0'

    def findKthBitV2(self, n: int, k: int) -> str:
        count = 0
        inv = 0
        if k < 4:
            return '0' if k == 1 else '1'
        while count < k:
            count = 2*count + 1
        while count > 3:
            if k > (count -1)//2:
                inv = 0
                k = k - (count - 1)//2 - 1
            else:
                inv = 1
            count = (count - 1)//2

        if k == 1:
            return '0' if inv else '1'
        elif inv:
            return '0' if k == 1 else '1'
        return '1' if k == 4 else '0'


#
# print(Solution().findKthBit(6, 44))
# print(Solution().findKthBitV2(6, 44))
print(Solution().findKthBitV2(4, 14))




