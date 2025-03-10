"""
Explanation:
    Merge sort is a divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
    The merge() function is used for merging two halves. The merge(arr, s, m, e) is a key process that assumes that arr[s..m] and arr[m+1..e] are sorted and merges the two sorted sub-arrays into one.
    The merge_sort(arr, s, e) function is a recursive function that sorts the given array from index s to e.
    The merge_sort() function first divides the array into two halves, then recursively sorts the two halves, and finally merges the two sorted halves.
    The merge_sort() function is called with the array, starting index, and ending index.
    The merge_sort() function returns the sorted array.
    The merge() function is called with the array, starting index, middle index, and ending index.
    The merge() function merges the two sorted halves of the array.
    The merge() function returns the merged array.
    The time complexity of the merge sort algorithm is O(n log n).
    The space complexity of the merge sort algorithm is O(n).
    The merge sort algorithm is stable.
"""


def merge_sort(arr, s, e):
    """
    Merge sort the given array
    """
    if e - s + 1 <= 2:
        return arr

    # split the array into two halves
    m = (s + e) // 2

    # sort the first half
    merge_sort(arr, s, m)

    # sort the second half
    merge_sort(arr, m + 1, s)

    # merge the two sorted halves together
    merge(arr, s, m, e)

    return arr


def merge(arr, s, m, e):
    """
    Merge the two sorted halves of the array
    """
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s : m + 1]
    R = arr[m + 1 : e + 1]

    i = 0  # index for L
    j = 0  # index for R
    k = s  # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array is", arr)
