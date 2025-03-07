def factorial(n: int):
    """
    Calculate the factorial of a number using recursion."
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))  # 120
    print(factorial(10))  # 3628800
