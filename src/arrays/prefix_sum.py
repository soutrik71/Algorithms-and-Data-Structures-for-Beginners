"""
Prefix Sum Array
Given an array of integers nums, calculate the prefix sum array.
The prefix sum array is defined as the array of running sums of nums.
That is, the ith element of the prefix sum array is the sum of the first i + 1 elements of nums.

"""


class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return preRight - preLeft


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    prefixSum = PrefixSum(nums)
    print(prefixSum.rangeSum(1, 3))
