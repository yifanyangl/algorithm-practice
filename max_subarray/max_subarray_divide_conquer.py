#!/usr/bin/env python3
# [Maximum Subarray - LeetCode](https://leetcode.com/problems/maximum-subarray/)
# Will time out using this implementation
# Check out book CLRS 4.1
import math


def max_subarray_dc(arr, start, end):
    if start < end - 1:
        mid = math.ceil((end + start) / 2)
        max_left = max_subarray_dc(arr, start, mid)
        max_right = max_subarray_dc(arr, mid, end)
        max_cross = max_subarray_dc_cross(arr, start, mid, end)
        return max(max_left, max_right, max_cross)
    else:
        return arr[start]


def max_subarray_dc_cross(arr, start, mid, end):
    max_left = -math.inf
    cur_sum = 0
    for i in range(mid - 1, -1, -1):
        cur_sum += arr[i]
        if cur_sum > max_left:
            max_left = cur_sum

    max_right = -math.inf
    cur_sum = 0
    for i in range(mid, end):
        cur_sum += arr[i]
        if cur_sum > max_right:
            max_right = cur_sum

    return max_left + max_right
