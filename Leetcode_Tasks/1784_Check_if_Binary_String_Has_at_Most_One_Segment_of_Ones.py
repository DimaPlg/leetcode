import unittest
from typing import List


class CheckIfBinaryStringHasAtMostOneSegment:
    def checkOnesSegment(self, s: str) -> bool:
        len_segment = 0
        for num in s:
            if num == '1' and len_segment == -1:
                return False
            elif num == '1':
                len_segment +=1
            elif  len_segment > 0 and num == '0':
                len_segment = -1
        return True

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sum_nums = ((1 + length)*length)//2
        sum_have = sum(set(nums))
        lost_num = sum_nums - sum_have
        return [lost_num - 1 if sum(nums) < sum_nums else  lost_num + 1  , lost_num]

# class TestCheckIfBinaryStringHasAtMostOneSegment(unittest.TestCase):
#     def test_checkOnesSegment(self):
#         date = [['1',1], ['1110011',0], ['111111000',1], ['1000000',1]]
#         for date, result in date:
#             try:
#                 self.assertEqual(CheckIfBinaryStringHasAtMostOneSegment().checkOnesSegment(date), result)
#             except AssertionError:
#                 print(date)
#
# if __name__ == '__main__':
#     unittest.main()

print(Solution().findErrorNums([2,2]))