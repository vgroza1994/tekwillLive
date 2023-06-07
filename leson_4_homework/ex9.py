"""
Scrieți un program care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""
parola=input('Introduceti parola:')

if len(parola) >= 8 and any(c.islower() for c in parola) and any(c.isupper() for c in parola):
    print("Parolă puternică")
else:
    print("Parolă slabă")