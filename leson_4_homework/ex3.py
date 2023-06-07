"""
Citiţi de la tastatură un număr întreg.
Dacă numărul este negativ, afişaţi mesajul `"That number is less than 0!"`.
Dacă este pozitiv, afişaţi `"That number is greater than 0!"`.
Dacă nu este nici negativ nici pozitiv afişaţi mesajul `"You picked 0!"`.
"""
a = int(input("a:"))


if a > 0:
    print(f"a: {a}The numbers are greater than 0")

if  a < 0:
    print(f"a:{a}That number is less than 0!")
if a == 0:
    print(f"a:{a}You picked 0!")