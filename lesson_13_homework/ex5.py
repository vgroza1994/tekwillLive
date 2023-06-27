class AgeError(Exception):
    pass


def get_age():
    try:
        age = int(input("Introduceți vârsta dvs.: "))

        if age < 0 or age > 150:
            raise AgeError("Vârsta introdusă nu este validă.")

        return age

    except ValueError:
        raise AgeError("Vârsta trebuie să fie un număr întreg.")



try:
    age = get_age()
    print("Vârsta introdusă:", age)

except AgeError as e:
    print("Eroare de vârstă:", str(e))