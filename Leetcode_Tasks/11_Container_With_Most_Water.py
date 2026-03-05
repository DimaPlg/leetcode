# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
import unittest
from typing import List


class ContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        max_height,left_board,right_board,step = max(height),-1,0,1
        length = len(height)
        max_area = 0
        for i in range(max_height,0,-1):
            for j in range(length):
                if height[j] > i - 1 and left_board ==-1:
                    left_board = j
                if height[-j - 1] > i - 1 and right_board ==0:
                    right_board = -j-1
                if  left_board > length + right_board -1:
                    left_board, right_board = -1, 0
                    break
                if left_board != -1 and right_board != 0:
                    if (length + right_board - left_board)*i > max_area:
                        max_area = (length + right_board - left_board)*i
                        left_board,right_board = -1,0
                        break
            left_board, right_board = -1, 0
        return max_area

    def maxAreaV2(self, height: List[int]) -> int:
        area = lambda x,y: (x - y)*(height[x] if height[x] < height[y] else height[y])
        length = len(height)
        max_height, left_board, right_board, step = max(height), 0, length-1, 1

        max_area = area(right_board, left_board)
        while left_board < right_board:
            if (area(right_board - 1, left_board) > area(right_board, left_board + 1) and
                    area(right_board - 1, left_board) > max_area):
                    max_area = area(right_board - 1, left_board)
                    right_board -= 1

            elif (area(right_board - 1, left_board) < area(right_board, left_board + 1) and
                  area(right_board, left_board + 1) > max_area):
                    max_area = area(right_board, left_board + 1)
                    left_board +=1
            else:
                if height[left_board] > (height[right_board] - 1):
                    right_board -= 1
                else:
                    left_board += 1

        return max_area

    def maxAreaV3(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        left_board, right_board = 0, length -1
        while left_board < right_board:
            max_area = max(max_area, min(height[left_board],height[right_board]) * (right_board - left_board))
            if height[left_board] > height[right_board]:
                right_board -= 1
            else:
                left_board += 1
        return max_area

class TestContainerWithMostWater(unittest.TestCase):
    def test_maxArea(self):
        date_cases = [[[1,8,6,2,5,4,8,3,7], 49], [[1,1], 1], [[1,2,3,1000,9], 9], [[1,3,2,5,25,24,5], 24]]
        for date, result in date_cases:
            
            self.assertEqual(ContainerWithMostWater().maxArea(date), result)

            self.assertEqual(ContainerWithMostWater().maxAreaV2(date), result)

            self.assertEqual(ContainerWithMostWater().maxAreaV3(date), result)



if __name__ == '__main__':
    unittest.main()

