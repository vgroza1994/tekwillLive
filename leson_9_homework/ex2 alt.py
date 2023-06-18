text = input("text:")

words = text.split()

num_total_cuvinte = len(words)

cuvinte_unice = set(words)

frecventa_cuvinte = {}

for cuvant in words:
    frecventa_cuvinte[cuvant] = frecventa_cuvinte.get(cuvant, 0) + 1

cuvinte_sortate = sorted(frecventa_cuvinte.items(), key=lambda x: x[1], reverse=True)

top_30_utilizate = cuvinte_sortate[:30]

top_30_puțin_utilizate = cuvinte_sortate[-30:]

print("Numărul total de cuvinte din text:", num_total_cuvinte)
print("Cele mai utilizate 30 de cuvinte:")
for cuvant, frecventa in top_30_utilizate:
    print(cuvant, "-", frecventa)

print("Cele mai puțin utilizate 30 de cuvinte:")
for cuvant, frecventa in top_30_puțin_utilizate:
    print(cuvant, "-", frecventa)
