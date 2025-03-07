def fibonacci(n: int):
    """
    Calculate the nth Fibonacci number using recursion.
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
