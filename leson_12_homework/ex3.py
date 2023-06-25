import re

def check_password_strength(password):

    if len(password) < 8:
        return False


    if not re.search(r'[A-Z]', password):
        return False


    if not re.search(r'[a-z]', password):
        return False


    if not re.search(r'\d', password):
        return False


    if not re.search(r'[!@#$%^&*]', password):
        return False

    return True


password = input("Introduceți o parolă: ")


password_strength = check_password_strength(password)


if password_strength:
    print("Puterea parolei: True (respectă criteriile)")
else:
    print("Puterea parolei: False (nu respectă criteriile)")