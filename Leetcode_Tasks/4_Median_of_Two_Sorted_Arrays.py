# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
import unittest
from typing import List


class MedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        center = (len_nums1 + len_nums2) / 2
        center = int(center) + 1
        res_list = []
        nums1_index = 0
        nums2_index = 0
        for i in range(center):
            if nums1_index > len_nums1 - 1:
                res_list.append(nums2[nums2_index])
                nums2_index += 1
                nums1_index += 1
            elif nums2_index > len_nums2 - 1:
                res_list.append(nums1[nums1_index])
                nums1_index += 1
                nums2_index += 1
            elif nums1[nums1_index] > nums2[nums2_index]:
                res_list.append(nums2[nums2_index])
                nums2_index +=1
            else:
                res_list.append(nums1[nums1_index])
                nums1_index +=1
        return (res_list[-1] + res_list[-2])/2 if (
                (len_nums1 + len_nums2) % 2 == 0) else (
                res_list[-1]/1)


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        self.assertEqual(MedianOfTwoSortedArrays().findMedianSortedArrays([1,3], [2]), 2.0)
        self.assertEqual(MedianOfTwoSortedArrays().findMedianSortedArrays([1,2], [3,4]), 2.5)
        self.assertEqual(MedianOfTwoSortedArrays().findMedianSortedArrays([], [2]), 2.0)
        self.assertEqual(MedianOfTwoSortedArrays().findMedianSortedArrays([2,3], []),2.5)
        self.assertEqual(MedianOfTwoSortedArrays().findMedianSortedArrays([], []),0.0)

if __name__ == '__main__':
    unittest.main()