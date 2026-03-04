# Given an m x n binary matrix mat, return the number of special positions in mat.
#
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j
# are 0 (rows and columns are 0-indexed).
import unittest
from typing import List


class SpecialPositions:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        for row in range(len(mat)):
            if sum(mat[row]) == 1:
                for col in range(len(mat[row])):
                    if mat[row][col] == 1 and sum(row[col] for row in mat) == 1:
                        res +=1
                        break
        return res

class TestClassSpecialPositions(unittest.TestCase):
    def test_numSpecial(self):
        self.assertEqual(SpecialPositions().numSpecial([[1,0,0],[0,0,1],[1,0,0]]), 1)
        self.assertEqual(SpecialPositions().numSpecial([[1,0,0],[0,1,0],[0,0,1]]), 3)

if __name__ == '__main__':
    unittest.main()