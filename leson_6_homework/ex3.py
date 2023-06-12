"""
Inbunatatiti acest generator de parole, astfel in cat sa fie posibil sa genereze parole ce contin atat litere,
 cat si cifre si caractere speciale.
"""

import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Exemplu de utilizare:
length = 12  # Lungimea parolei dorite
password = generate_password(length)
print(password)