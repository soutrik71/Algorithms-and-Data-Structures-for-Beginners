"""
Sliding Window (Fixed)
The idea behind having a fixed sliding window is to maintain two pointers that are k apart from each other and fit a certain constraint.

Motivation
Q: Given an array, return true if there are two elements within a window of size k
k that are equal.
Let's say that we have the array [1,2,3,2,3,3], with k = 3. The window of size 3 is [1,2,3]. We can see that there are two elements that are equal, 2 and 3. Therefore, the output should be True.
"""

# first we apply brute force approach and then sliding window approach


def contains_duplicate_brute_force(nums, k):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True


def closeDuplicatesWindow(nums, k):
    window = set()
    L = 0
    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1

        if nums[R] in window:
            return True

        window.add(nums[R])

    return False


if __name__ == "__main__":
    # nums = [1, 2, 3, 2, 3, 3]
    nums = [1, 2, 3, 1]
    k = 3
    # print(contains_duplicate_brute_force(nums, k))
    print(closeDuplicatesWindow(nums, k))
