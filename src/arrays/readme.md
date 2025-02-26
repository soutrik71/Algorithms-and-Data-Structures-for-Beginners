# Static Arrays

- **Definition:**  
  - Fixed-size arrays in statically typed languages (e.g., Java, C++, C#)
  - Size and type are determined at initialization and cannot change

## Key Operations & Time Complexities

### 1. Reading from an Array

- **Operation:** Access an element by its index
- **Time Complexity:** O(1)
- **Example:**

  ```python
  myArray = [1, 3, 5]
  element = myArray[i]  # Direct access via index i
  ```

### 2. Traversing an Array

- **Operation:** Iterate over all elements
- **Time Complexity:** O(n)
- **Example:**

  ```python
  for i in range(len(myArray)):
      print(myArray[i])
  ```

### 3. Deleting from an Array

#### a. Deleting from the End

- **Operation:** Overwrite the last element with a default value (e.g., 0, -1, or null) and decrement the length.
- **Time Complexity:** O(1)
- **Example:**

  ```python
  def removeEnd(arr, length):
      if length > 0:
          arr[length - 1] = 0  # Soft delete by marking as empty
  ```

#### b. Deleting at an Arbitrary Index

- **Operation:** Remove element at index i by shifting subsequent elements left.
- **Time Complexity:** O(n) (worst-case when deleting the first element)
- **Example:**

  ```python
  def removeMiddle(arr, i, length):
      for index in range(i + 1, length):
          arr[index - 1] = arr[index]
  ```

### 4. Inserting into an Array

#### a. Inserting at the End

- **Operation:** Place the new element at the next available index (current length), if capacity permits.
- **Time Complexity:** O(1)
- **Example:**

  ```python
  def insertEnd(arr, n, length, capacity):
      if length < capacity:
          arr[length] = n
  ```

#### b. Inserting at an Arbitrary Index

- **Operation:** Shift existing elements to the right starting from index i to make room for the new element.
- **Time Complexity:** O(n)

# Dynamic Arrays

- **Definition:**
  - Arrays that can grow dynamically as elements are added.
  - Default in languages like JavaScript and Python.
  - No need to specify a size upon initialization (though some languages may start with a default size, e.g., Java: 10, C#: 4).

## Insertion & Resizing

### Insertion at the End

- **Process:**
  - Check if `length == capacity`.
    - If yes, call `resize()` to expand the array.
  - Insert the new element at the next empty index.
- **Example:**

  ```python
  def pushback(self, n):
      if self.length == self.capacity:
          self.resize()
      self.arr[self.length] = n
      self.length += 1
  ```

### Resize Operation

- **Process:**
  - Double the current capacity.
  - Create a new array with the new capacity.
  - Copy all elements from the old array to the new one.
  - Replace the old array with the new array.
- **Example:**

  ```python
  def resize(self):
      self.capacity = 2 * self.capacity
      newArr = [0] * self.capacity 
      for i in range(self.length):
          newArr[i] = self.arr[i]
      self.arr = newArr
  ```

## Amortized Time Complexity

- **Insertion:**  
  - Most insertions are O(1).
  - Occasional resize operations are O(n), but over many operations, the *amortized* time per insertion is O(1).
- **Doubling Strategy:**  
  - Starting from a small array (e.g., size 1), the capacity grows as 1 → 2 → 4 → 8 → ...  
  - The total cost to insert n elements is O(n) due to the doubling strategy (sum of powers of 2 ≤ 2n).

## Other Operations

- **Access:**  
  - O(1) time.
- **Insertion/Deletion in the Middle:**  
  - Requires shifting elements, resulting in O(n) time.

## Summary of Time Complexities

| Operation               | Time Complexity | Notes                                          |
|-------------------------|-----------------|------------------------------------------------|
| **Access**              | O(1)          | Direct index access                             |
| **Insertion at End**    | O(1)*         | Amortized O(1); O(n) when resizing is needed     |
| **Insertion in Middle** | O(n)          | Due to shifting elements                        |
| **Deletion at End**     | O(1)          | Soft deletion by overwriting                    |
| **Deletion in Middle**  | O(n)          | Due to shifting elements                        |

*Insertion and deletion at the end are O(1) in most cases.

# Stacks

- **Definition:**
  - A stack is a dynamic data structure that operates on a LIFO (Last In, First Out) basis.
  - Elements can only be added or removed from one end: the top of the stack.
  - Often implemented using dynamic arrays.

## Key Operations

### 1. Push

- **Purpose:** Add an element to the top of the stack.
- **Time Complexity:** O(1)
- **Example:**

  ```python
  def push(self, n):
      self.stack.append(n)
  ```

### 2. Pop

- **Purpose:** Remove and return the top element from the stack.
- **Time Complexity:** O(1)
- **Note:** Check if the stack is empty before popping.
- **Example:**

  ```python
  def pop(self):
      return self.stack.pop()
  ```

### 3. Peek

- **Purpose:** Return the top element without removing it.
- **Time Complexity:** O(1)
- **Example:**

  ```python
  def peek(self):
      return self.stack[-1]
  ```

## Time Complexity Summary

| Operation   | Time Complexity | Notes                                 |
|-------------|-----------------|---------------------------------------|
| **Push**    | O(1)            | Add element to the top                |
| **Pop**     | O(1)            | Remove element from the top (check for empty) |
| **Peek**    | O(1)            | Retrieve the top element without removing it |


# Kadane's Algorithm

Kadane's algorithm is a greedy/dynamic programming approach used to find the maximum sum subarray in an array. It efficiently computes the maximum subarray sum in **O(n)** time by making just one pass through the array.

---

## Motivation

**Problem:** Find a non-empty subarray (i.e., contiguous elements) with the largest sum.

A brute force solution would involve checking every possible subarray and computing its sum. For an array of length *n*, this approach results in **O(n²)** time complexity:

```python
def bruteForce(nums):
    maxSum = nums[0]
    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum
```

Although this works, it's inefficient for large inputs.

---

## Kadane's Algorithm: The Intuition

1. **All Positive Numbers:**  
   If all elements are positive, the maximum sum subarray is the entire array.

2. **Handling Negatives:**  
   Negative numbers decrease the overall sum. However, sometimes including a negative number is necessary to reach subsequent positive numbers. For example:
   - For `[6, -2, 7]`, the maximum sum is `11` (including the `-2`).
   - For `[1, -3, 7]`, the maximum sum is `7` (excluding the `-3`).

**Key Idea:**  
If the current subarray sum becomes negative, it is better to start a new subarray from the next element, as the negative sum would only drag down any further addition.

---

## Kadane's Algorithm Implementation

```python
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        # If the current sum is negative, discard it and start fresh.
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum
```

### Explanation

- **Initialization:**  
  `maxSum` is initialized to the first element to handle cases where all numbers are negative. `curSum` starts at `0`.

- **Iteration:**  
  For each number in the list, reset `curSum` to `0` if it is negative before adding the current number. Then update `maxSum` if `curSum` exceeds it.

- **Edge Case:**  
  If every element is negative, `maxSum` will correctly be the largest negative number.

---

## Sliding Window Variant

Sometimes, you might need to return the actual subarray with the maximum sum, not just the sum itself. This can be done by keeping track of the indices defining the subarray (a "window").

```python
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0  # To store the indices of the max subarray
    L = 0  # Left pointer of the current window

    for R in range(len(nums)):
        # If current sum is negative, reset and start a new window from index R.
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]  # Returns the starting and ending indices of the max subarray
```

### Explanation

- **Window Pointers:**  
  `L` and `R` denote the boundaries of the current window (subarray).  
  `maxL` and `maxR` store the indices of the subarray with the maximum sum found so far.

- **Logic:**  
  If the current sum `curSum` drops below `0`, reset it and move the left pointer `L` to the current index `R`. Update the maximum sum and indices when a new maximum is found.

---

## Time & Space Complexity

- **Time Complexity:**  
  Both the standard and sliding window approaches run in **O(n)** time because they process the array with a single pass.

- **Space Complexity:**  
  **O(1)** extra space is used since only a few variables are maintained regardless of the input size.

---

## Closing Notes

Kadane's algorithm is a powerful technique for solving maximum subarray problems efficiently. The sliding window variant further extends its utility by providing the exact subarray boundaries when needed. These techniques can also serve as a foundation for understanding more advanced problems that involve dynamic programming or variable-sized sliding windows.

# Sliding Window (Fixed)

The idea behind a fixed sliding window is to maintain two pointers that are `k` apart and satisfy a certain constraint.

---

## Motivation

**Problem:**  
Given an array, return `True` if there are two elements within a window of size `k` that are equal.

A brute-force solution would consider every subarray of size `k` and check for duplicates. For example, with the array `[1, 2, 3, 2, 3, 3]` and `k = 3`, the brute-force approach would inspect each possible subarray of size `k`.

---

## Brute-Force Approach

```python
def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False
```

This approach results in a time complexity of **O(n\*k)** (or **O(n²)** in the worst case).

---

## Sliding Window Approach

We can optimize the brute-force solution using a sliding window along with a hash set. The set will store unique elements in the current window, enabling **O(1)** lookups.

**Strategy:**

- Maintain a window (using two pointers) that never exceeds size `k`.
- As the window slides, remove the element that falls out of the window.
- If a new element is already in the set (i.e., it's a duplicate within the window), return `True`.

### Implementation

```python
def closeDuplicates(nums, k):
    window = set()  # Current window of size <= k
    L = 0

    for R in range(len(nums)):
        # Ensure the window size does not exceed k
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        # If the element is already in the window, a duplicate exists
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False
```

---

## Time and Space Complexity

- **Time Complexity:**  
  The algorithm performs a single pass through the array, resulting in **O(n)** time. Each set operation (lookup, addition, and removal) is **O(1)** on average.

- **Space Complexity:**  
  The space used is **O(k)** since the set holds at most `k` distinct elements.

# Sliding Window (Variable Size)

Another variation of the sliding window technique is the variable size sliding window. This is useful when we don't have a fixed window size and need to keep expanding our window as long as it meets a certain constraint.

---

## Simple Example

**Problem:**  
Find the length of the longest subarray where every element is the same.

**Approach:**  
- Use two pointers, `L` and `R`, to define the current window.
- The constraint is that all values in the window must be identical.
- Start at the beginning and expand the window from the right.
- When a new value is encountered (i.e., `nums[L] != nums[R]`), reset the window by setting `L` to `R`.
- Update the maximum length using the current window size (`R - L + 1`).

**Code Example:**

```python
def longestSubarray(nums):
    length = 0
    L = 0
    
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R 
        length = max(length, R - L + 1)
    return length
```

