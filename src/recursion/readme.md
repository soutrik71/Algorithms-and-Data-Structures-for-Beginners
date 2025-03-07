## **Recursion (One Branch)**

Recursion is when a function calls itself, usually with a different input. It helps break down problems into smaller sub-problems and solves them in reverse order.

### **Key Components of Recursion**

- **Base case**: The stopping condition.
- **Recursive case**: The function calls itself with modified input.

### **Factorial Example (Recursive)**

```python
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case
```

**Execution Breakdown (factorial(5)):**

```
factorial(5) → 5 * factorial(4)
factorial(4) → 4 * factorial(3)
factorial(3) → 3 * factorial(2)
factorial(2) → 2 * factorial(1)  # Base case reached
factorial(1) → 1
```

Final computation: `5 * 4 * 3 * 2 * 1 = 120`

### **Time & Space Complexity**

- **Time:** O(n) → `n` calls to `factorial(n)`
- **Space:** O(n) → `n` function calls on the stack

### **Iterative Approach**

```python
n = 5
res = 1
while n > 1:
    res *= n
    n -= 1
```

- More **space-efficient** than recursion (O(1) space).
- Easier to understand in some cases.

### **Key Takeaways**

- Recursion is useful for problems with **self-similar structure**.
- Always define a **base case** to prevent infinite recursion.
- Iterative solutions can be **more efficient** in some cases.

## **Recursion (Two Branches)**

### **Fibonacci Sequence**

The Fibonacci sequence starts with `0` and `1`, where each subsequent number is the sum of the two preceding numbers:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

Mathematically, it's defined as:

- **Base cases**:  
  - `F(0) = 0`  
  - `F(1) = 1`
- **Recursive case**:  
  - `F(n) = F(n - 1) + F(n - 2)`

### **Recursive Implementation**

```python
def fibonacci(n):
    if n <= 1:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
```

This function calls itself twice, leading to an **exponential growth** of recursive calls.

### **Execution Breakdown**

To compute `fibonacci(5)`, we break it down recursively:

```
fibonacci(5) → fibonacci(4) + fibonacci(3)
fibonacci(4) → fibonacci(3) + fibonacci(2)
fibonacci(3) → fibonacci(2) + fibonacci(1)
...
```

#### **How It Works**

1. The function repeatedly calls itself for smaller values of `n`, forming a **recursion tree**.
2. Once `n = 0` or `n = 1`, the function stops (base case).
3. It then **combines** results from the smaller sub-problems to compute the final result.

The tree expands exponentially, solving smaller sub-problems and combining results as it moves back up.

### **Time & Space Complexity**

- **Time Complexity**:  
  - O(2ⁿ) → **Exponential time** due to redundant calculations.
- **Space Complexity**:  
  - O(n) → Due to recursive call stack.

### **Key Takeaways**

- **Inefficient for large `n`** because of redundant calculations.
- **Better approach**: **Memoization** or **Dynamic Programming** to store computed values and reduce complexity.
