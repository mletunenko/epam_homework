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
        return 0
    max_s = None
    for w_size in range(1, k + 1):
        for i in range(len(nums) - w_size + 1):
            w = nums[i:i + w_size]
            s = sum(w)
            if max_s is None:
                max_s = s
                continue
            if s > max_s:
                max_s = s
    return max_s
