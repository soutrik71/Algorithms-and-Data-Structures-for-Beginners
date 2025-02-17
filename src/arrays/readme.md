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