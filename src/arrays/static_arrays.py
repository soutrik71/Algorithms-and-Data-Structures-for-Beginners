

Algorithms and Data Structures for Beginners
2 / 35











































































2 - Static Arrays

Suggested Problems

Status
Star
Problem   
Difficulty   
Solution
Remove Duplicates From Sorted Array	
Remove Element	
Static Arrays
In statically typed languages like Java, C++ and C#, arrays have to have an allocated size and type when initialized. These are known as static arrays.

They are called static because the size of the array cannot change once declared. And once the array is full, it can not store additional elements. Some dynamically typed languages such as Python and JavaScript do not have static arrays to begin with. They have an alternative, which we will discuss in the next lesson.

Let's cover the key operations of an array, and the time complexity associated with each.

Reading from an array
To read an individual element from an array we can choose the position we want to access via an index. Below we have initialized an array of size 3 called myArray. We also attempt to access an arbitrary element using the index i.

# initialize myArray
myArray = [1,3,5]

# access an arbitrary element, where i is the index of the desired value
myArray[i]
reading-from-array

Accessing a single element in an array is always instant because each index of myArray is mapped to an address in the RAM. Regardless of the size of the input array, the time taken to access a single element is the same. We refer to this operation as 
O
(
1
)
O(1) in terms of time complexity.

There is a common confusion that 
O
(
1
)
O(1) is always fast. This is not the case. There could be 
1000
1000 operations and the time complexity could still be 
O
(
1
)
O(1). If the number of operations does not grow as the size of the data or input grows then it is 
O
(
1
)
O(1).
Traversing through an array
We can also read all values within an array by traversing through it. Below are examples of how we could traverse myArray from the start to the end using loops.

for i in range(len(myArray)):
   print(myArray[i])

# OR

i = 0
while i < len(myArray):
   print(myArray[i])
   i += 1
The last element in an array is always at index 
n
−
1
n−1 where 
n
n is the size of the array. If the size of our array is 
3
3, the last accessible index is 
2
2.
To traverse through an array of size 
n
n the time complexity is 
O
(
n
)
O(n). This means the number of operations grows linearly with the size of the array.

For example, with an array of size 10 we would have to perform 10 operations to traverse through it, with an array of size 100 we would have to perform 100 operations, and so on.

Deleting from an array
Deleting from the end of the array

In statically typed languages, all array indices are filled with 0s or some default value upon initialization, denoting an empty array.

When we want to remove an element from the last index of an array, setting its value to 0 / null or -1 is the best we can do. This is known as a soft delete. The element is not being "deleted" per se, but it is being overwritten by a value that denotes an empty index. We will also reduce the length by 1 since we have one less element in the array after deletion. The code below demonstrates the concept using [4, 5, 6] as an example.

# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr, length):
    if length > 0:
        # Overwrite last element with some default value.
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0
deletion-at-end

6
6 is deleted/overwritten by either 
0
0 or 
−
1
−1 to denote that it does not exist anymore. Length is also decremented by 
1
1.
Deleting at an ith index

If instead of deleting at the end, we wanted to delete an element at a random index i. Would we be able to perform this in 
O
(
1
)
O(1)?

We could naively just replace it with a 0, but this would break the contiguous nature of our array. Notice that deleting from the end of an array doesn't make it non-contigious, but deleting from the middle will.

A better approach would be the following:

We are given the deletion index i.
We iterate starting from i + 1 until the end of the array.
We shift each element 1 position to the left.
(Optional) We replace the last element with a 0 or null to mark it empty, and decrement the length by 1.
The following code demonstrates this operation.

# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted
removal-0th-index

The worst case would be that we need to shift all of the elements to the left. This would occur if the target index is the first index of the array. Therefore, the code above is 
O
(
n
)
O(n).
Insertion
Inserting at the end

If we want to insert an element at the end of the array, we can simply insert it at the next open position which will be at index length where length is the number of elements in the array.

# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n
Since we are writing a single value to the array, the time complexity is 
O
(
1
)
O(1).
Note: length is the number of elements inside the array whereas capacity refers to the maximum number of elements the array can hold.

Inserting at the ith index

Inserting at an arbitrary index i is more involved since we may insert in the middle of the array.

Consider the array [4, 5, 6]. If we need to insert at index i = 1, or i = 0, we cannot overwrite the original value because we would lose it. Instead, we will need to shift all values, starting at index i, one position to the right. Below is the code and visual demonstrating this.

# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    
    # Insert at i
    arr[i] = n
The below image visualizes the insertion of 8 at index 1 in the array [4, 5, 6]. Since we don't have enough space to keep the last element 6, it is lost.

insertion-at-i

The visual above demonstrates that shifting occurs prior to insertion to ensure values are not overwritten.
Time Complexity
Operation	Big-O Time	Notes
Reading	
O
(
1
)
O(1)	
Insertion	
O
(
n
)
O(n)*	If inserting at the end of the array, 
O
(
1
)
O(1)
Deletion	
O
(
n
)
O(n)*	If deleting at the end of the array, 
O
(
1
)
O(1)
Closing Notes
The operations we discussed above are absolutely critical for solving a lot of interview problems. In fact, the key to solving many problems is being able to implement the insert middle and delete middle operations efficiently.

There are some suggested problems listed above. If you are a beginner you may find them challenging. That's completely okay, your goal should be to understand the concepts and the operations we discussed above. The solution code and video explanation are provided for each problem.

# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr, length):
    if length > 0:
        # Overwrite last element with some default value.
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0

# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    
    # Insert at i
    arr[i] = n

# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted

def printArr(arr, capacity):
    for i in range(capacity):
        print(arr[i])