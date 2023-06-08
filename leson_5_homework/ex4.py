"""
Creaţi 2 liste: `elev1` şi `elev2`.

Pentru fiecare elev, cititi de la tastatură **numele**, **prenumele** şi **nota** obţinută la examen şi salvaţi datele în listele `elev1` şi `elev2`.

După aceasta, afişaţi la ecran:
* care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi prenumele)
* care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi prenumele)
* pentru fiecare elev, transformaţi numele sa fie scris cu toate literele majuscule, iar prenumele să înceapă cu literă mare. De exemplu, pentru elevul "Elon Musk", rezultatul afişat va fi "Elon MUSK"
*	afişaţi datele sub formă de tabel, folosind indexarea listelor, ca în exemplul de mai jos (Nu neaparat sa fie tabel):

| Elon | Musk | 9.5 |
|------|------|-----|
| Bill | Gates | 8.5|
"""
elev1 = []
elev2 = []


nume_elev1 = input("Introduceți numele elevului 1: ")
prenume_elev1 = input("Introduceți prenumele elevului 1: ")
nota_elev1 = float(input("Introduceți nota obținută de elevul 1: "))


elev1.append([nume_elev1, prenume_elev1, nota_elev1])


nume_elev2 = input("Introduceți numele elevului 2: ")
prenume_elev2 = input("Introduceți prenumele elevului 2: ")
nota_elev2 = float(input("Introduceți nota obținută de elevul 2: "))


elev2.append([nume_elev2, prenume_elev2, nota_elev2])


if nota_elev1 > nota_elev2:
    elev_cu_nota_mai_mare = elev1
    elev_cu_nota_mai_mica = elev2
elif nota_elev1 < nota_elev2:
    elev_cu_nota_mai_mare = elev2
    elev_cu_nota_mai_mica = elev1
else:
    print("Ambele elevi au obținut aceeași notă.")

for i in range(len(elev1)):
    elev1[i][0] = elev1[i][0].upper()
    elev1[i][1] = elev1[i][1].capitalize()

for i in range(len(elev2)):
    elev2[i][0] = elev2[i][0].upper()
    elev2[i][1] = elev2[i][1].capitalize()


print("Elevul cu nota mai mare: ", elev_cu_nota_mai_mare[0][0], elev_cu_nota_mai_mare[0][1])
print("Elevul cu nota mai mică: ", elev_cu_nota_mai_mica[0][0], elev_cu_nota_mai_mica[0][1])


print("| {:<4} | {:<6} | {:<4} |".format("Nume", "Prenume", "Nota"))
print("|-------|--------|------|")
for elev in elev1:
    print("| {:<4} | {:<6} | {:<4} |".format(elev[0], elev[1], elev[2]))
for elev in elev2:
    print("| {:<4} | {:<6} | {:<4} |".format(elev[0], elev[1], elev[2]))