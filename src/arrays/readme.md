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



