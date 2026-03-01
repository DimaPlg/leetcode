# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
# For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
#
# Given a string n that represents a positive decimal integer,
# return the minimum number of positive deci-binary numbers needed so that they sum up to n.
import unittest


class Partitioning_Deci_Binary:
    def minPartitions(self, n: str) -> int:
        return int(max(set(n)))

class TestPartitioning_Deci_Binary(unittest.TestCase):
    def test_minPartitions(self):
        self.assertEqual(Partitioning_Deci_Binary().minPartitions('32'), 3)
        self.assertEqual(Partitioning_Deci_Binary().minPartitions('82734'), 8)
        self.assertEqual(Partitioning_Deci_Binary().minPartitions('27346209830709182346'), 9)

if __name__ == '__main__':
    unittest.main()