### **Insertion Sort (Simplified with Explanation)**

#### **Concept**

Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time. It works well for **small** or **nearly sorted** datasets but is inefficient for large datasets.

#### **How It Works**

1. Assume the **first element** is sorted.
2. Pick the **next element** and insert it into its correct position in the sorted part of the array.
3. Repeat this process for all elements.

#### **Algorithm (Python Implementation)**

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:  # Swap if out of order
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr
```

#### **Example**

Sorting `[2,3,4,1,6]` step by step:

1. `[2]` → Already sorted
2. `[2,3]` → Sorted
3. `[2,3,4]` → Sorted
4. `[2,3,4,1]` → Insert `1` in the correct position → `[1,2,3,4]`
5. `[1,2,3,4,6]` → Sorted

#### **Key Properties**

- **Stable Sorting Algorithm** → Maintains the relative order of duplicate elements.
- **Works for Any Data Type** (as long as comparisons are possible).
- **In-Place Sorting** → Uses **O(1)** extra space.

#### **Time Complexity**

- **Best Case:** \( O(n) \) → Already sorted array.
- **Worst/Average Case:** \( O(n^2) \) → Elements are in reverse order or random.

#### **Space Complexity**

- \( O(1) \) → No extra space is used.

Insertion Sort is useful for **small datasets** or **nearly sorted data**, but for larger datasets, more efficient sorting algorithms like Merge Sort or Quick Sort are preferred.

### **Merge Sort (With Explanation)**

#### **Concept**

Merge Sort is a **divide and conquer** sorting algorithm. It recursively **splits** the array into halves until each subarray contains only one element. Then, it **merges** these subarrays back together in sorted order.

#### **How It Works**

1. **Divide**: Recursively split the array into two halves.
2. **Conquer**: Recursively sort each half.
3. **Combine**: Merge the sorted halves back into a single sorted array.

#### **Algorithm (Python Implementation)**

```python
# Merge Sort function
def merge_sort(arr, s, e):
    if e - s + 1 <= 1:  # Base case: Array with 1 or no elements is already sorted
        return

    m = (s + e) // 2  # Find the middle index

    merge_sort(arr, s, m)      # Sort the left half
    merge_sort(arr, m + 1, e)  # Sort the right half
    merge(arr, s, m, e)        # Merge the sorted halves

# Merge function
def merge(arr, s, m, e):
    L = arr[s:m + 1]  # Left half
    R = arr[m + 1:e + 1]  # Right half

    i, j, k = 0, 0, s  # Pointers for left, right, and merged array

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:  # Maintain stability
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):  # Copy remaining elements from L
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):  # Copy remaining elements from R
        arr[k] = R[j]
        j += 1
        k += 1
```

#### **Example**

Sorting `[3,2,4,1,6]` step by step:

1. Split into `[3,2,4]` and `[1,6]`
2. Further split into `[3,2]`, `[4]`, `[1]`, `[6]`
3. `[3,2]` → Sort to `[2,3]`
4. Merge `[2,3]` with `[4]` → `[2,3,4]`
5. Merge `[1]` with `[6]` → `[1,6]`
6. Merge `[2,3,4]` with `[1,6]` → `[1,2,3,4,6]` (sorted)

#### **Key Properties**

- **Stable Sorting Algorithm** → Maintains relative order of duplicate elements.
- **Works for Any Data Type** (as long as comparisons are possible).
- **Out-of-Place Sorting** → Uses extra space for merging.

#### **Time Complexity**

- **Best Case:** \( O(n \log n) \) → Even if the array is already sorted.
- **Worst/Average Case:** \( O(n \log n) \) → Always splits and merges.

#### **Space Complexity**

- \( O(n) \) → Uses additional space for merging.

#### **Comparison with Insertion Sort**

| Sorting Algorithm | Best Case | Worst Case | Average Case | Space Complexity |
|------------------|-----------|------------|-------------|------------------|
| **Insertion Sort** | \( O(n) \) | \( O(n^2) \) | \( O(n^2) \) | \( O(1) \) (In-place) |
| **Merge Sort** | \( O(n \log n) \) | \( O(n \log n) \) | \( O(n \log n) \) | \( O(n) \) (Uses extra space) |

🔹 **Use Insertion Sort** when the array is small and nearly sorted.  
🔹 **Use Merge Sort** when sorting large datasets due to its guaranteed \( O(n \log n) \) time complexity.

### **Quick Sort (With Explanation)**

#### **Concept**

Quick Sort is a **divide and conquer** sorting algorithm. It selects a **pivot** and partitions the array such that:

- Elements **less than or equal** to the pivot move to the left.
- Elements **greater than** the pivot move to the right.
- Recursively, this process repeats for left and right subarrays.

Unlike Merge Sort, Quick Sort does not require merging, as the partitioning step inherently sorts the array.

#### **How It Works**

1. **Choose a Pivot**:
   - Last element (simplest approach).
   - First element.
   - Median of first, middle, and last element.
   - Random pivot (reduces worst-case likelihood).

2. **Partitioning**:
   - Rearrange elements so that all smaller ones go left and larger ones go right.
   - Place the pivot in its correct position.

3. **Recursively Apply Quick Sort**:
   - Apply the same process to left and right subarrays.

#### **Algorithm (Python Implementation)**

```python
# Quick Sort function
def quick_sort(arr, s, e):
    if e - s + 1 <= 1:  # Base case: Single-element array is already sorted
        return

    pivot = arr[e]  # Choosing the last element as pivot
    left = s  # Pointer for smaller elements

    # Partitioning step
    for i in range(s, e):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    # Place pivot in its correct position
    arr[left], arr[e] = arr[e], arr[left]

    # Recursively sort left and right partitions
    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)
```

#### **Example**

Sorting `[6,2,4,1,3]` step by step:

1. **Pick Pivot:** `3` (last element).
2. **Partitioning:** `[2,1]` (left) | `3` (pivot) | `[6,4]` (right).
3. **Recursively Sort Left & Right:** `[1,2]` and `[4,6]`.
4. **Final Sorted Array:** `[1,2,3,4,6]`.

#### **Key Properties**

- **Not Stable** → May swap non-adjacent elements.
- **In-Place Sorting** → No extra memory allocation (modifies array in place).
- **Efficient on Average** → Performs well with **random pivots**.

#### **Time Complexity**

| Case | Complexity | Explanation |
|------|------------|------------|
| **Best Case** | \( O(n \log n) \) | Balanced partitioning (pivot splits the array in half). |
| **Average Case** | \( O(n \log n) \) | Random pivot selection usually ensures good partitioning. |
| **Worst Case** | \( O(n^2) \) | Pivot always smallest/largest → Uneven partitions. |

#### **Space Complexity**

- \( O(\log n) \) → Due to recursive calls (depth of recursion tree).

#### **Comparison with Merge Sort**

| Sorting Algorithm | Best Case | Worst Case | Average Case | Space Complexity | Stability |
|------------------|-----------|------------|-------------|------------------|-----------|
| **Merge Sort** | \( O(n \log n) \) | \( O(n \log n) \) | \( O(n \log n) \) | \( O(n) \) (Extra space) | ✅ Stable |
| **Quick Sort** | \( O(n \log n) \) | \( O(n^2) \) | \( O(n \log n) \) | \( O(\log n) \) (In-place) | ❌ Not Stable |

🔹 **Use Quick Sort** when sorting large datasets and in-place sorting is needed.  
🔹 **Use Merge Sort** when stability is required or when working with linked lists.
