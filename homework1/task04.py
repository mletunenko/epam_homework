"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that
A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(
        a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    zero_count = 0
    for av in a:
        for bv in b:
            for cv in c:
                for dv in d:
                    if av + bv + cv + dv == 0:
                        zero_count += 1
    return zero_count
