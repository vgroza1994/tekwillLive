def generate_fibonacci(terms):
    fibonacci_sequence = [0, 1]


    while len(fibonacci_sequence) < terms:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence



terms = int(input("Introduceți numărul de termeni Fibonacci de generat: "))


fibonacci_sequence = generate_fibonacci(terms)


print("Secvența Fibonacci generată:", fibonacci_sequence)
