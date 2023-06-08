"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**, **prenumele**, **vârsta**, **înălţimea** şi **ocupaţia** utilizatorului şi adăugaţi aceste valori în lista creată.
"""
date_personale =[]
for date in range(1):
    numele=input(f"Nume persoana:{date}! ")\

    prenumele = input(f"Prenumele:{date}!")\

    virsta = input(f"Virsta:{date}!")\

    inaltimea = input(f"Inaltimea:{date}!")\

    ocupatia = input(f"Ocupatia:{date}!")


    print(numele,prenumele,virsta,inaltimea,ocupatia)
    date_personale.append((numele,prenumele,virsta,inaltimea,ocupatia))
    print(date_personale)