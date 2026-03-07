import random
import time
import unittest
from typing import List


class SmallerNumCurrent:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        control_dict = {}
        nums_sorted = sorted(nums)
        res_list = []
        counter = 0
        for num in nums_sorted:
            if num not in control_dict:
                control_dict[num] = 1
            else:
                control_dict[num] += 1

        for num in nums:
            for key in control_dict:
                if key < num:
                    counter += control_dict[key]
                else:
                    res_list.append(counter)
                    counter = 0
                    break
        return res_list

    def smallerNumbersThanCurrentV2(self, nums: List[int]) -> List[int]:
        control_dict = {}
        nums_sorted = sorted(nums)
        counter = 0
        for num in nums_sorted:
            if num not in control_dict:
                control_dict[num] = counter
                counter = control_dict[num] + 1
            else:
                counter +=1
        return [control_dict[num] for num in nums]



class TestSmallerNumCurrent(unittest.TestCase):

    def test_smallerNumbersThanCurrent(self,):
        test_date = [[[6, 5, 4, 8], [2, 1, 0, 3]], [[8, 1, 2, 2, 3], [4, 0, 1, 1, 3]], [[7, 7, 7, 7], [0, 0, 0, 0]]]
        for date, results in test_date:
            try:
                self.assertEqual(SmallerNumCurrent().smallerNumbersThanCurrent(date), results)
            except AssertionError:
                print(f'first version, date: {date}')

            try:
                self.assertEqual(SmallerNumCurrent().smallerNumbersThanCurrentV2(date), results)
            except AssertionError:
                print(f'second version, date: {date}')

    def test_time_smallerNumbersThanCurrent(self, times = 100):
        startv1 = time.perf_counter()
        for  i in range(times):
            SmallerNumCurrent().smallerNumbersThanCurrent(
                [random.randint(1, 1000) for _ in range(random.randint(100, 500))])
        endv1 = time.perf_counter()
        startv2 = time.perf_counter()
        for i in range(times):
            SmallerNumCurrent().smallerNumbersThanCurrentV2(
                [random.randint(1, 1000) for _ in range(random.randint(100, 500))])
        endv2 = time.perf_counter()
        duration1 = endv1 - startv1
        duration2 = endv2 - startv2
        if duration1 < duration2:
            print(f'First solution faster on: {duration2 - duration1} per {times} times')
        else:
            print(f'Second solution faster on: {duration1 - duration2} per {times} times')

if __name__ == '__main__':
    unittest.main()