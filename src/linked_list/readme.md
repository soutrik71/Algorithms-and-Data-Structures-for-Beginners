# Linked List

A **linked list** is a data structure that consists of a sequence of elements, where each element points to the next element in the sequence. It is a **linear data structure** used to store elements. Each element in a linked list is called a **node**, which contains:

- **Data**
- **A reference (pointer) to the next node** in the sequence

The first node is called the **head**, and the last node is called the **tail**. The **tail node points to null**.

## Types of Linked Lists

There are two types of linked lists:
1. **Singly Linked List**: Each node points only to the next node in the sequence.
2. **Doubly Linked List**: Each node points to both the next node **and** the previous node in the sequence.

## Advantages & Disadvantages of Linked Lists

### **Advantages**
- **Dynamic Size**: Can grow and shrink in size dynamically.
- **Efficient Insertions/Deletions**: Can be easily inserted and deleted without shifting elements.

### **Disadvantages**
- **Memory Overhead**: Requires extra memory for pointers.
- **Slower Access Time**: Elements are not stored contiguously in memory, requiring traversal.

## Applications of Linked Lists
- **Implementing other data structures** (e.g., stacks, queues, graphs).
- **Algorithms** (e.g., sorting, graph traversal).

## Example: Singly Linked List in Python

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

llist = LinkedList()
llist.append(1)
llist.append(2)

llist.print_list()
```

This code creates a **singly linked list** with two nodes containing the data values `1` and `2`, then prints the data values of the nodes.

---

# Doubly Linked Lists

A **doubly linked list** is a variation of the singly linked list where each node has **two pointers**:
- `next` pointer (points to the next node)
- `prev` pointer (points to the previous node)

If the `prev` pointer points to `null`, it indicates that we are at the **head** of the linked list.

## Operations of a Doubly Linked List

### **Insertion at the End**
Adding a node to a doubly linked list runs in **O(1)** time. However, we must update both the `next` and `prev` pointers.

Example:
```python
tail.next = ListNode4
ListNode4.prev = tail
tail = tail.next
```

### **Insertion at the Front** *(Animation Needed)*

### **Deletion at the End**
Deleting at the end is also an **O(1)** operation.

**Steps:**
1. Get a reference to the node before the tail.
2. Update the `next` pointer of the node before the tail to `null`.
3. Update the `tail` to be the node before the tail.
4. *(Optional)* Update the `prev` pointer of the old tail to `null`.

Example:
```python
ListNode2 = tail.prev
ListNode2.next = null
tail = ListNode2
```

Since **insertion and deletion at the end run in O(1) time**, a **stack** could be implemented with a linked list instead of an array.

### **Deletion at the Front** *(Animation Needed)*

### **Accessing Nodes**
Similar to singly linked lists, we **cannot randomly access** a node. The worst case requires traversing **n** nodes before reaching the desired node, resulting in **O(n)** time complexity.

However, unlike singly linked lists, **doubly linked lists allow traversal in both directions**.

## **Closing Notes**

| Operation  | Big-O Time Complexity | Notes |
|------------|----------------------|----------------------------|
| **Access** | O(n) | - |
| **Search** | O(n) | - |
| **Insertion** | O(1) | *Assuming you have a reference to the node at the desired position* |
| **Deletion** | O(1) | *Assuming you have a reference to the node at the desired position* |

