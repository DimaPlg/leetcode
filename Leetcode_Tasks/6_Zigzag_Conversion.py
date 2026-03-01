# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
import unittest

class ZigzagConv:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res_list =[]
        length = len(s)
        position = 0
        counter = 0
        while length > len(res_list):
            if position > length + numRows and counter < numRows - 2:
                position = 0
                counter += 1
                if length > position - counter > -1:
                    res_list.append(s[position - counter])
                if position + counter < length:
                    res_list.append(s[position + counter])
            elif position < length + numRows and numRows - 1 > counter > 0:
                if length > position - counter > -1:
                    res_list.append(s[position - counter])
                if position + counter < length:
                    res_list.append(s[position + counter])
            else:
                if position > length -1:
                    position = 0
                    counter += 1
                res_list.append(s[position + counter])
            position += 2 * numRows - 2
        return ''.join(res_list)

class TestZigzagConv(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(ZigzagConv().convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(ZigzagConv().convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
        self.assertEqual(ZigzagConv().convert('AB', 1), 'AB')
        self.assertEqual(ZigzagConv().convert('AB', 2), 'AB')
        self.assertEqual(ZigzagConv().convert('ABCD', 3), 'ABDC')

if __name__ == '__main__':
    unittest.main()


