def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number recursively.

    Args:
        n (int): The position of the Fibonacci number.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")