# Minimum-on-the-segment
Given an array of n integers and a window of size k, output the minimum element for each contiguous subarray of length k. Solved in O(n) time using a deque that maintains indices with non-decreasing values, removing outdated indices from the front and larger values from the back.
