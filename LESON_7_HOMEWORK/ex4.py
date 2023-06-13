"""Scrieți un program care utilizează o buclă while pentru a verifica dacă un număr întreg pozitiv dat n este un număr prim.
 Un număr prim este un număr întreg pozitiv mai mare decât 1 care nu are divizori pozitivi în afară de 1 și el însuși.
  Programul ar trebui să afișeze dacă numărul este prim sau nu.
  """


numar = int(input("Introduceți un număr întreg: "))

if numar <= 1:
    print(numar, "nu este un număr prim.")
else:
    este_prim = True
    divizor = 2

    while divizor <= numar // 2 and este_prim:
        if numar % divizor == 0:
            este_prim = False
        divizor += 1

    if este_prim:
        print(numar, "este un număr prim.")
    else:
        print(numar, "nu este un număr prim.")
