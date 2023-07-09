'''Creati un program care va permite inregistrarea unui client.

Utilizatorul va introduce Numele, Prenumele si Ziua de naster a clientului in formatul 20/01/1930

Programul trebuie sa afiseze urmatoarea Clientul Nume, Prenume va avea ziua de nastere in n zile unde n este numarul de zile pan la urmatoarea zi de nastere a clientului.'''

import datetime


def calcul_zile_nastere(nume, prenume, data_nasterii):
    data_nasterii = datetime.datetime.strptime(data_nasterii, "%d/%m/%Y")
    an_nastere = data_nasterii.year
    data_urmatoare_nastere = datetime.datetime(datetime.datetime.today().year, data_nasterii.month, data_nasterii.day)

    if data_urmatoare_nastere < datetime.datetime.today():
        data_urmatoare_nastere = datetime.datetime(datetime.datetime.today().year + 1, data_nasterii.month,
                                                   data_nasterii.day)

    numar_zile = (data_urmatoare_nastere - datetime.datetime.today()).days

    print("Clientul", nume, prenume, "va avea ziua de naștere în", numar_zile, "zile.")



nume = input("Introduceți numele clientului: ")
prenume = input("Introduceți prenumele clientului: ")
data_nasterii = input("Introduceți ziua de naștere a clientului (format: DD/MM/YYYY): ")


calcul_zile_nastere(nume, prenume, data_nasterii)