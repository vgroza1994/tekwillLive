#'''Scrieți un program care utilizează o buclă while pentru a calcula factorialul unui număr întreg pozitiv dat n.
#Factorialul unui număr este produsul tuturor numerelor întregi pozitive de la 1 la n.
''
n = int(input("Introduceți un număr întreg pozitiv: "))

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print("Factorialul numărului", n, "este:", factorial)