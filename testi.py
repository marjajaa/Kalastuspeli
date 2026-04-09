import random
from reppu_luokka import Reppu
from kala_luokka import Kala

reppu = Reppu()

kalalajit = ["kuha", "ahven", "taimen", "lohi", "hauki", "siika"]
paino = [random.uniform(0.1, 15) for x in range(40)]
salaatit = ["Sait merilevää", "Syötti irtosi", "Siima katkesi"]


def kalastaminen():
    todennäköisyys = random.random()
    if todennäköisyys <= 0.70:
        saalis = random.choice(kalalajit)
        saaliin_paino = round(random.choice(paino), 3)

        print(f"Nappasit: {saalis}, {saaliin_paino}kg")

        k1 = Kala(saalis, saaliin_paino)
        reppu.lisaa(k1)

        peliin()

    else:
        salaatti = random.choice(salaatit)
        print(salaatti)
        peliin()



def peliin():

    while True:
        print("Valitse 1, jos haluat kalastaa")
        print("Valitse 2, jos tarkastaa repun sisällön")

        valinta = input("Valitse 1 tai 2: ")

        if valinta == "1":
            print("Aloitit kalastamisen")
            kalastaminen()
            break
        
        elif valinta == "2":
            print(reppu.merkkijonona())
            
            break

    #repussa on kalat ja syötit


def paavalikko():

    while True:
        
        print("Päävalikko")
        print("Valitse 1, jos haluat aloittaa kalastamisen")
        print("Valitse 2, jos haluat poistua pelistä")
        print("Valitse 3, jos haluat mennä kauppaan")

        valinta = input("Valitse 1, 2 tai 3: ")
        print(f"debug {valinta}")

        if valinta == "1":
            print("Siirrytään peliin....")
            peliin()
            break


        elif valinta == "2":
            print("Poistutaan valikosta")
            break

        if valinta == "3":
            print("Mennään kauppaan...")
            break

        else:
            print("Syötä numero 1, 2 tai 3!")


paavalikko()








