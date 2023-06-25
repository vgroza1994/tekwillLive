def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Solicităm utilizatorului să introducă un număr
num = int(input("Introduceți un număr: "))

# Apelăm funcția is_prime cu valoarea introdusă
if is_prime(num):
    print(num, "este un număr prim.")
else:
    print(num, "nu este un număr prim.")