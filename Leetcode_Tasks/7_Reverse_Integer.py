# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.
import unittest


class ReverseInteger:
    def reverse(self, x: int) -> int:
        counter = 1
        res = 0
        minus = 0 if x > 0 else 1
        x = abs(x)
        while x > 0:
            res = ((res * 10) + (x % 10))
            x //= 10
        if -(2**31) > res or res > (2**31):
            return 0
        return res if minus == 0 else -res

    def reverseV2(self, x: int) -> int:
        if -2147483648 > x or x > 2147483648:
            return 0
        minus = 0 if x > 0 else 1
        x = abs(x)
        res = int(str(x)[::-1])
        if -2147483648 > res or res > 2147483647:
            return 0
        return res if minus == 0 else -res

class TestReverseInteger(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(ReverseInteger().reverse(0), 0)
        self.assertEqual(ReverseInteger().reverse(-1), -1)
        self.assertEqual(ReverseInteger().reverse(1243), 3421)

        self.assertEqual(ReverseInteger().reverseV2(0), 0)
        self.assertEqual(ReverseInteger().reverseV2(-1), -1)
        self.assertEqual(ReverseInteger().reverseV2(1243), 3421)

        self.assertEqual(ReverseInteger().reverse(-2147483), ReverseInteger().reverseV2(-2147483))

if __name__ == '__main__':
    unittest.main()