"""
Kadane's Algorithm
Kadane's algorithm is a greedy/dynamic programming algorithm that can be used on an array. It is used to calculate the maximum sum subarray ending at a particular position and typically runs in O(n) time complexity.
"""

# Q: Find a non-empty subarray with the largest sum.
# First we approach with the brute force solution
# Then we will implement Kadane's algorithm
# They we apply a variation of Kadane's algorithm to find the subarray with the largest sum using sliding window technique

from typing import List, Optional, Union


def brute_force(nums: list):
    """
    Brute force: What we are trying to do is to find the sum of all possible subarrays and return the maximum sum.
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    max_sum = nums[0]
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(curr_sum, max_sum)

    return max_sum


def kadane(nums: List[int]):
    """
    Kadane's algorithm: We are trying to find the maximum sum subarray using a pointer to keep track of the current sum and the maximum sum.
    We reset the current sum to 0 if it becomes negative and add the current element to the current sum.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    max_sum = nums[0]
    curr_sum = 0
    for n in nums:
        curr_sum = max(curr_sum, 0)
        curr_sum += n
        max_sum = max(curr_sum, max_sum)

    return max_sum


def sliding_window(nums: list[int]):
    """
    Sliding window: We are trying to find the subarray with the largest sum using the sliding window technique.
    We keep track of the left and right pointers and move the right pointer to the right until the sum is greater than the maximum sum.
    If the sum becomes negative, we reset the sum to 0 and move the left pointer to the right.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    max_sum = nums[0]
    curr_sum = 0
    maxl, maxr = 0, 0
    left = 0

    for right in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            left = right

        curr_sum += nums[right]
        if curr_sum > max_sum:
            max_sum = curr_sum
            maxl = left
            maxr = right

    return [maxl, maxr]


if __name__ == "__main__":
    nums = [4, -1, 2, -7, 3, 4]
    print(brute_force(nums))
    print(kadane(nums))
    print(sliding_window(nums))
