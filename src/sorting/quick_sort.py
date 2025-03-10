"""
Explanation:

    Quick sort is a divide and conquer algorithm that selects a pivot element and partitions the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
    The quick_sort() function is used to sort the given array.
    The quick_sort() function is a recursive function that sorts the given array from the start index to the end index.
    The quick_sort() function first selects a pivot element and partitions the array into two sub-arrays.
    The quick_sort() function then recursively sorts the two sub-arrays.
    The quick_sort() function returns the sorted array.
    The partition() function is used to partition the array into two sub-arrays.
    The partition() function selects the last element as the pivot element.
    The partition() function then partitions the array into two sub-arrays according to whether they are less than or greater than the pivot.
    The partition() function returns the index of the pivot element.
    The time complexity of the quick sort algorithm is O(n log n) in the average case and O(n^2) in the worst case.
    The space complexity of the quick sort algorithm is O(log n).
    The quick sort algorithm is not stable.
"""


def quick_sort(arr: list[int], start: int, end: int):
    """
    Quick sort algorithm implementation
    :param arr: list of integers
    :param start: start index
    :param end: end index
    :return: sorted list
    """
    # base criteria
    if end - start + 1 <= 1:
        return arr

    # set pivot and pointer
    pivot = arr[end]
    left = start

    # we do the swapping to left if less than pivot else right
    for i in range(start, end):
        if arr[i] < pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1

    # now we place the pivot back to last pointer position and swapping it
    arr[end] = arr[left]
    arr[left] = pivot

    # now we do recursive sorting of left
    quick_sort(arr, start, left - 1)

    # quick sort of right
    quick_sort(arr, left + 1, end)

    return arr


if __name__ == "__main__":
    arr = [3, 2, 1, 5, 4]
    print(quick_sort(arr, 0, len(arr) - 1))  # Output: [1, 2, 3, 4, 5]

    arr = [3, 2, 1, 5, 4, 7, 6]
    print(quick_sort(arr, 0, len(arr) - 1))  # Output: [1, 2, 3, 4, 5, 6, 7]
