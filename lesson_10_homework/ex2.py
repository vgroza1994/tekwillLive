numar_oaspeti = int(input('Numar oaspeti:'))
oaspeti={"Vitalie":'pizza,steak.',"Ion":'pasta,bors.',"Marina":'pizza,sarmale.'}
totaluri=dict()
for key,value in oaspeti.items():
    print(f'Nume:{key},\n Feluri:{value}')
    feluri = value.split(',')
    for fel in feluri:
        fel = fel.strip()
        totaluri[fel] = totaluri.get(fel, 0) + 1

print(totaluri)