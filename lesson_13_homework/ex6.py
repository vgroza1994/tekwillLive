import math


def calculate_geometric_mean(numbers):
    if 0 in numbers:
        raise ZeroDivisionError("Lista conține zero.")

    product = 1
    for num in numbers:
        product *= num

    geometric_mean = math.pow(product, 1 / len(numbers))
    return geometric_mean
numbers1 = [2, 4, 8, 16]
print(calculate_geometric_mean(numbers1))

numbers2 = [1, 2, 3, 0, 4, 5]
print(calculate_geometric_mean(numbers2))