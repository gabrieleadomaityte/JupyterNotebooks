# 1 užduotis
# Parašykite funkciją, kuri kaip argumentą priima vieną kintamąjį (tekstą) ir grąžina jį apversta
# pavyzdžiui, pateikus žodį "labas", funkcija grąžintų atsakymą "sabal"
# pateikus žodį "alus", grąžintų "sula"
# parašykite keletą testų šiai funkcijai
# 2 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina to sąrašo narių sumą
# parašykite keletą testų šiai funkcijai
# 3 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina jame esančius TEIGIAMUS skaičius
# parašykite keletą testų šiai funkcijai
# 4 užduotis
# Parašykite funkciją, kuri priima dvi sąrašų rūšiavimo funkcijas: vieną didėjančiai rūšiavimui, 
# kitą mažėjančiai rūšiavimui, ir sąrašą skaičių. 
# Funkcija turi grąžinti rūšiuotą sąrašą pagal pateiktas rūšiavimo funkcijas.
# parašykite keletą testų šiai funkcijai

def apversta(tekstas):
    return tekstas[::-1]

def sar_suma(sarasas:list):
    return sum(sarasas)

def sar_teigiami(sarasas:list):
    return [i for i in sarasas if i >0]


def isrikiuoti(f:str, sarasas:list) -> list:
    def rikiuoti_mazejanciai(sarasas):
        return sorted(sarasas, reverse=True)
    
    def rikiuoti_didejant(sarasas):
        return sorted(sarasas)

    if f == 'didejant':
        return rikiuoti_didejant(sarasas)
    else:
        return rikiuoti_mazejanciai(sarasas)

print(isrikiuoti('didejant', [1,5,2]))

# pateikiame funkcija kaip argumenta 

def apskaiciuoti(funkcija, skaicius1, skaicius2):
    return funkcija(skaicius1, skaicius2)

def sudetis(num1, num2):
    return num1 + num2

def daugyba(num1, num2):
    return num1 * num2

print(apskaiciuoti(sudetis, 5,10))

def rikiuoti(rikiavimo_funkcija, sarasas):
    return rikiavimo_funkcija(sarasas)

def rikiuoti_mazejanciai(sarasas):
    return sorted(sarasas, reverse=True)
    
def rikiuoti_didejant(sarasas):
    return sorted(sarasas)

print(rikiuoti(rikiuoti_mazejanciai, [5,3,4,1,6,9]))

# 1 Užduotis
# Sukurkite funkciją, kuri patikrintų ar skaičius dalinasi iš 3
# Parašykite keletą testų (naudojantis parametrize)
# 2 užduotis 
# Parašykite funkciją rasti_pasikartojancias_raides, kuri priima sąrašą žodžių ir grąžina sąrašą tų žodžių
# kurie turi bent vieną pasikartojančią raidę.
# Parašykite keletą testų (naudojantis parametrize)
# 3 užduotis 
# Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis. 
# Grąžinkite True, jei skaičius yra pirminis, ir False, jei ne.
# Parašykite keletą testų (naudojantis parametrize)

def dalyba_3(a):
    return 'Dalinasi' if a%3 == 0 else 'Nesidalina'

def rasti_pasikartojancias_raides(zodziai):
    pasikartojantys = []
    for zodis in zodziai:
        for raide in zodis:
            if zodis.count(raide) >1:
                pasikartojantys.append(zodis)
                break
    return pasikartojantys

def pirminis(a):
    if a <=1:
        return False
    for i in range(2,a):
        if a%i == 0:
            return False
    return True

