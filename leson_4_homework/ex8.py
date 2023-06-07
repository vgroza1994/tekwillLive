"""
Scrieți un program care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""
text= input()

if text.endswith("?"):\
        print("Aceasta este o întrebare")
else:\
        print("Aceasta nu este o întrebare")