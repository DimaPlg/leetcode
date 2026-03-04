# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
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
            if area(right_board - 1, left_board) > max_area:
                max_area = area(right_board - 1, left_board)
                right_board -= 1
            elif area(right_board, left_board + 1) > max_area:
                max_area = area(right_board, left_board + 1)
                left_board +=1
            else:
                right_board -= 1
                left_board += 1

        return max_area




print(ContainerWithMostWater().maxAreaV2([1,8,6,2,5,4,8,3,7]))