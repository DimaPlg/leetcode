import unittest


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

class TestCheckIfBinaryStringHasAtMostOneSegment(unittest.TestCase):
    def test_checkOnesSegment(self):
        date = [['1',1], ['1110011',0], ['111111000',1], ['1000000',1]]
        for date, result in date:
            try:
                self.assertEqual(CheckIfBinaryStringHasAtMostOneSegment().checkOnesSegment(date), result)
            except AssertionError:
                print(date)

if __name__ == '__main__':
    unittest.main()