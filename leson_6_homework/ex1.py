"""
Calculator BMI
Scrie un program care primește greutatea unei persoane (în kilograme) și înălțimea (în metri) ca intrare și calculează Indicele de Masă Corporală (BMI). Apoi clasifică BMI-ul în următoarele categorii:

Subponderal (BMI < 18,5)
Greutate normală (BMI între 18,5 și 24,9)
Supraponderal (BMI între 25 și 29,9)
Obezitate (BMI 30 sau mai mare)

Pentru a calcula Indicele de Masă Corporală (BMI), urmează pașii de mai jos:

1. Ia greutatea persoanei în kilograme și înălțimea în metri.
2. Calculează pătratul înălțimii (înmulțește înălțimea cu ea însăși).
3. Calculează BMI-ul utilizând formula: BMI = greutate / înălțime^2, unde greutatea este în kilograme și înălțimea este în metri.
4. Rezultatul obținut va fi indicele de masă corporală al persoanei.

"""
def calculate_bmi(greutate, inaltime):
    inaltime_squared = inaltime ** 2
    bmi = greutate / inaltime_squared
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Subponderal"
    elif 18.5 <= bmi < 25:
        return "Greutate normală"
    elif 25 <= bmi < 30:
        return "Supraponderal"
    else:
        return "Obezitate"

greutate = float(input("Introduceți greutatea (în kilograme): "))
inaltime = float(input("Introduceți înălțimea (în metri): "))

bmi = calculate_bmi(greutate, inaltime)
classification = classify_bmi(bmi)

print("Indicele de Masă Corporală (BMI) este:", bmi)
print("Clasificare BMI:", classification)