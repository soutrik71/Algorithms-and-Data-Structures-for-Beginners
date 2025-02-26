# Static Arrays

## Definition
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
- **Time Complexity:** O(1)
- **Example:**
  ```python
  def removeEnd(arr, length):
      if length > 0:
          arr[length - 1] = 0  # Soft delete by marking as empty
  ```

#### b. Deleting at an Arbitrary Index
- **Time Complexity:** O(n)
- **Example:**
  ```python
  def removeMiddle(arr, i, length):
      for index in range(i + 1, length):
          arr[index - 1] = arr[index]
  ```

### 4. Inserting into an Array

#### a. Inserting at the End
- **Time Complexity:** O(1)
- **Example:**
  ```python
  def insertEnd(arr, n, length, capacity):
      if length < capacity:
          arr[length] = n
  ```

#### b. Inserting at an Arbitrary Index
- **Time Complexity:** O(n)

---

# Dynamic Arrays

## Definition
- Arrays that can grow dynamically as elements are added.
- Default in languages like JavaScript and Python.
- No need to specify a size upon initialization.

## Insertion & Resizing

### Insertion at the End
- **Time Complexity:** Amortized O(1)
- **Example:**
  ```python
  def pushback(self, n):
      if self.length == self.capacity:
          self.resize()
      self.arr[self.length] = n
      self.length += 1
  ```

### Resize Operation
- **Time Complexity:** O(n)
- **Example:**
  ```python
  def resize(self):
      self.capacity = 2 * self.capacity
      newArr = [0] * self.capacity
      for i in range(self.length):
          newArr[i] = self.arr[i]
      self.arr = newArr
  ```

## Summary of Time Complexities
| Operation               | Time Complexity |
|-------------------------|----------------|
| **Access**              | O(1)           |
| **Insertion at End**    | O(1)*          |
| **Insertion in Middle** | O(n)           |
| **Deletion at End**     | O(1)           |
| **Deletion in Middle**  | O(n)           |

---

# Stacks

## Definition
- A stack is a LIFO data structure.
- Often implemented using dynamic arrays.

## Key Operations

### 1. Push
- **Time Complexity:** O(1)
- **Example:**
  ```python
  def push(self, n):
      self.stack.append(n)
  ```

### 2. Pop
- **Time Complexity:** O(1)
- **Example:**
  ```python
  def pop(self):
      return self.stack.pop()
  ```

### 3. Peek
- **Time Complexity:** O(1)
- **Example:**
  ```python
  def peek(self):
      return self.stack[-1]
  ```

---

# Kadane's Algorithm

## Definition
Kadane's algorithm finds the maximum sum subarray in **O(n)** time.

## Implementation
```python
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0
    for n in nums:
        curSum = max(curSum, 0) + n
        maxSum = max(maxSum, curSum)
    return maxSum
```

---

# Sliding Window (Fixed & Variable Size)

## Fixed Window
- Maintains a window of size `k`.
- **Example:** Check if two elements within a window are equal.
```python
def closeDuplicates(nums, k):
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
```

## Variable Window
- Expands and contracts dynamically based on conditions.
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

---

# Two Pointers

## Example: Check Palindrome
```python
def isPalindrome(word):
    L, R = 0, len(word) - 1
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1
    return True
```

## Example: Two Sum (Sorted Array)
```python
def targetSum(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        current_sum = nums[L] + nums[R]
        if current_sum > target:
            R -= 1
        elif current_sum < target:
            L += 1
        else:
            return [L, R]
```

---

# Prefix Sums

## Definition
A prefix sum array allows efficient range sum queries.

### Implementation
```python
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
        return (preRight - preLeft)
```

## Complexity
- **Building Prefix Sum:** O(n)
- **Querying Range Sum:** O(1)

---

# Closing Notes
- **Static arrays** are fixed-size, whereas **dynamic arrays** grow dynamically.
- **Stacks** use LIFO operations.
- **Kadane’s algorithm** finds max subarray sum in O(n).
- **Sliding window & two pointers** optimize array traversal.
- **Prefix sums** allow quick subarray sum queries.

These techniques are fundamental for efficient problem-solving in competitive programming and real-world applications.

