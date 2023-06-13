#"""Scrieți un program care utilizează o buclă while pentru a genera secvența Fibonacci până la un număr dat de termeni.
#Secvența Fibonacci este o serie de numere în care fiecare număr este suma celor două numere precedente. Secvența începe cu 0 și 1."""

termen_dorit=int(input('Introdiceti termenul dorit:'))
fibonacci=[0,1]
while len(fibonacci)<termen_dorit:
    numar_nou=fibonacci[-1]+fibonacci[-2]
    fibonacci.append(numar_nou)
    print("Secventa Fibonacci pina la termenul",termen_dorit,"este:")
    print(fibonacci)

