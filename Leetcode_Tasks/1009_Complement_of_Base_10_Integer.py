# The complement of an integer is the integer you get when you flip all the 0's to 1's
# and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.
import unittest


class BaseInteger:
    def bitwiseComplement(self, n: int) -> int:
        counter = 0
        for i in range(n + 1):
            counter += 2**i
            if counter > n - 1:
                return counter - n


class TestBaseInteger(unittest.TestCase):
    data = [[7, 0], [5, 2], [10, 5], [0, 1]]

    def __init__(self, value):
        super().__init__()
        self.value = value

    @classmethod
    def add_data(cls, item):
        cls.data.append(item)

    def test_basic(self, data):

