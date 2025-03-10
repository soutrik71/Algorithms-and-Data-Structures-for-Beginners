"""
Explanation:

    Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
    The insertion_sort() function is used to sort the given array in ascending order.
    The insertion_sort_2() function is used to sort the given array in descending order.
    The insertion_sort() function starts from the second element of the array and compares it with the previous elements.
    If the current element is smaller than the previous element, then it swaps the two elements.
    The insertion_sort_2() function is similar to the insertion_sort() function, but it sorts the array in descending order.
    The time complexity of the insertion sort algorithm is O(n^2) in the worst-case scenario.
    The space complexity of the insertion sort algorithm is O(1).
    The insertion sort algorithm is stable.
"""


def insertion_sort(array: list) -> list:
    """
    This function implements the insertion sort algorithm to sort a list of numbers in ascending order.

    :param array: A list of numbers.
    :return: A sorted list of numbers.
    """

    for i in range(1, len(array)):
        j = i - 1

        while j >= 0 and array[j + 1] < array[j]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
            j = j - 1

    return array


def insertion_sort_desc(array: list) -> list:
    """
    This function implements the insertion sort algorithm to sort a list of numbers in descending order.

    :param array: A list of numbers.
    :return: A sorted list of numbers.
    """

    for i in range(1, len(array)):
        j = i - 1

        while j >= 0 and array[j + 1] > array[j]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
            j = j - 1

    return array


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    print(insertion_sort(array))  # Output: [5, 6, 11, 12, 13]
    print(insertion_sort_desc(array))  # Output: [13, 12, 11, 6, 5]
    array = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(array))  # Output: [1, 2, 3, 4, 5, 6]
    print(insertion_sort_desc(array))  # Output: [6, 5, 4, 3, 2, 1]
