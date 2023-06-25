def is_valid_email(email):
    if email.count('@') != 1:
        return False

    parts = email.split('@')
    domain = parts[1]

    if '.' not in domain:
        return False

    domain_parts = domain.split('.')
    if len(domain_parts[-1]) < 2:
        return False

    return True
email = input("Introduceți adresa de email: ")

if is_valid_email(email):
    print("Adresa de email este validă.")
else:
    print("Adresa de email nu este validă.")