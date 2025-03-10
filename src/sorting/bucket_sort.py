"""
Bucket sort is a sorting algorithm that works by distributing the elements of an array into a number of buckets.
Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.
The time complexity of the bucket sort algorithm is O(n + k), where n is the number of elements in the array and k is the number of buckets.
The space complexity of the bucket sort algorithm is O(n + k).
The bucket sort algorithm is unstable.
"""


def bucketSort(arr):
    """
    Bucket sort algorithm implementation"
    """
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr


if __name__ == "__main__":
    arr = [2, 1, 0, 1, 2, 0, 1, 2, 0]
    print(bucketSort(arr))  # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]
