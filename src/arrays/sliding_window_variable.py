"""
Sliding Window (Variable Size)
Another variation of the sliding window technique is the variable size sliding window. This is useful when we don't have a fixed window size and we need to keep expanding our window as long as our window meets a certain constraint or condition.
"""


# Find the length of the longest subarray with the same value in each position.
def longest_subarray_same_value(nums):
    L = 0
    max_length = 0
    for R in range(len(nums)):
        if nums[R] != nums[L]:
            L = R
        max_length = max(max_length, R - L + 1)

    return max_length


# Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive.
def min_lenth_subarray(nums, target):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    L = 0
    total = 0
    min_length = float("inf")

    for R in range(len(nums)):
        total += nums[
            R
        ]  # expand the window to the right until we reach the target sum or greater

        if (
            total >= target
        ):  # shrink the window from the left until we reach the minimum length subarray that meets the target sum or greater
            min_length = min(min_length, R - L + 1)  # update the minimum length
            total -= nums[L]  # shrink the window
            L += 1  # move the left pointer to the right

    return 0 if min_length == float("inf") else min_length


if __name__ == "__main__":
    nums = [4, 2, 2, 3, 3, 3]
    print(longest_subarray_same_value(nums))
    print(min_lenth_subarray(nums, 6))
