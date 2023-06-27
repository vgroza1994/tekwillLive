try:
    num1 = float(input("Introduceți primul număr: "))
    num2 = float(input("Introduceți al doilea număr: "))

    if num2 == 0:
        raise ZeroDivisionError("Eroare: Impartirea la zero nu este permisă.")

    result = num1 / num2
    print("Rezultatul împărțirii: ", result)

except ValueError:
    print("Eroare: Introduceți numere valide.")
except ZeroDivisionError as e:
    print(e)