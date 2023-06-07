"""
Scrieți un program pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat în funcție de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""
temperatura = float(input("Introduceți temperatura: "))

if temperatura >= 40:
    mesaj = "Este extrem de cald."
elif temperatura >= 30:
    mesaj = "Este foarte cald."
elif temperatura >= 20:
    mesaj = "Vreme caldă."
elif temperatura >= 10:
    mesaj = "Vreme normală."
elif temperatura >= 0:
    mesaj = "Vreme rece."
elif temperatura >= -10:
    mesaj = "Vreme foarte rece."
else:
    mesaj = "Vreme extrem de rece."

print(mesaj)