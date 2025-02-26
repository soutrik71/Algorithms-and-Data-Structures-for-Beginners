"""
Two Pointers
We have already seen a variation of the two pointers technique when we learned about the sliding window, which also involves two pointers.

The main idea is to have a L (left) pointer and a R pointer, both starting at some indices of the array. They don't always have to start at the beginning of the array, as is common in the sliding window technique. The L and R pointers can start at any index of the array.

Concept
We will start the L pointer at 0 and R pointer at arr.length - 1 and increment either the L, or decrement R or both depending on the conditions given in the problem. This repeats until the pointers meet each other.
"""


# first we check palindrome using two pointers
def check_palindrome(s):
    """
    You return True if the string is a palindrome, otherwise False even if one character is different
    """
    L = 0
    R = len(s) - 1

    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1

    return True


# Given a sorted input array, return the two indices of two elements which sums up to the target value. Assume there's exactly one solution.
def two_sum(arr, target):
    """
    The reason we decrement R to make the sum smaller is because every number to the left of arr[R] is smaller than arr[R]. By the same token, every number to the right of arr[L] is greater than arr[L].
    """
    L = 0
    R = len(arr) - 1

    while L < R:
        if arr[L] + arr[R] > target:
            R -= 1

        elif arr[L] + arr[R] < target:
            L += 1

        else:
            return [L, R]


if __name__ == "__main__":
    print(check_palindrome("racecar"))
    print(check_palindrome("racecarr"))

    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([2, 3, 4], 7))  # [1, 2]
