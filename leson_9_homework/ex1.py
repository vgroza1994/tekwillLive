"""Creați două liste care vor reprezenta numele participanților la două evenimente. Transformați-le apoi în seturi.

Utilizați operațiile cu seturi și afișați rezultatele:

câți participanți au fost prezenți la ambele evenimente
câți participanți au fost prezenți doar la primul eveniment
câți participanți au fost prezenți doar la al doilea eveniment"""

eneviment_1 = input('Patricipantii la eveniment 1:').split()
eveniment_2 = input("Participantii eveniment 2:").split()
setul_1=set(eneviment_1)
setul_2=set(eveniment_2)
print(setul_1)
print(setul_2)
print('Participantii la ambele evenimente:',len(setul_1.union(setul_2)))
doar_primul_eveniment = setul_1.difference(setul_2)
doar_al_doilea_eveniment = setul_2.difference(setul_1)
numar_participanti_primul_eveniment = len(doar_primul_eveniment)
numar_participanti_al_doilea_eveniment = len(doar_al_doilea_eveniment)
print("Numărul de participanți prezenți doar la primul eveniment:", numar_participanti_primul_eveniment)
print("Numărul de participanți prezenți doar la al doilea eveniment:", numar_participanti_al_doilea_eveniment)