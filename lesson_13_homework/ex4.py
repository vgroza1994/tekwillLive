def calculate_factorial(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a positive integer.")

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    return factorial
print(calculate_factorial(5))
print(calculate_factorial(0))
print(calculate_factorial(3))

print(calculate_factorial(5.5))
print(calculate_factorial(-2)) 