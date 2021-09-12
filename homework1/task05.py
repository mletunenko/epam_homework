"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    # Check that given list is not empty
    if not nums:
        return None
    max_sum = None
    for window_size in range(1, k + 1):
        for i in range(len(nums) - window_size + 1):
            window = nums[i:i + window_size]
            window_sum = sum(window)
            if max_sum is None:
                max_sum = window_sum
                continue
            if window_sum > max_sum:
                max_sum = window_sum
    return max_sum
