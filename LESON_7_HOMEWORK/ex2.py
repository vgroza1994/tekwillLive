#'''Scrieți un program care generează un număr aleatoriu între 1 și 100 și permite utilizatorului să ghicească numărul.
# Programul ar trebui să furnizeze feedback ("mai mare" sau "mai mic") până când utilizatorul ghicește numărul corect.
# Programul ar trebui, de asemenea, să țină evidența numărului de încercări necesare pentru ca utilizatorul să ghicească corect.''''''
import random

numar_aleatoriu = random.randint(1, 100)
numar_incercari=0
ghicit=False
print("Ghiceste numaril intre 1 si 100.")
while not ghicit:
    number_guess=int(input("Introdu un numar:"))
    numar_incercari+=1
    if number_guess == numar_aleatoriu:
        print('Felicitari!Aighicit numarul',numar_incercari,"incercari.")
        break
    elif number_guess<numar_aleatoriu:
        print("Numarul introdus este prea mic. Incearca din nou.")
    else:
        print('Numarul introdus este prea mare.Incearca din nou')

