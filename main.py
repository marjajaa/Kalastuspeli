import random
from reppu_luokka import Reppu
from kala_luokka import Kala

reppu = Reppu()

kalalajit = ["kuha", "ahven", "taimen", "lohi", "hauki", "siika"]
paino = [random.uniform(0.1, 15) for x in range(40)]
salaatit = ["Sait merilevää", "Syötti irtosi", "Siima katkesi"]
syotit = 3
siimat = 3
tili = 0

def kalastaminen(syotit, siimat):
    todennäköisyys = random.random()
    
    if syotit > 0 and siimat > 0:

        if todennäköisyys <= 0.70:
            syotit = syotit - 1
            saalis = random.choice(kalalajit)
            saaliin_paino = round(random.choice(paino), 3)

            print(f"Nappasit: {saalis}, {saaliin_paino}kg")

            k1 = Kala(saalis, saaliin_paino)
            reppu.lisaa(k1)

            peliin(syotit, siimat, tili)

        else:
            syotit = syotit - 1
            salaatti = random.choice(salaatit)

            if salaatti == "Siima katkesi":
                siimat = siimat - 1

            print(salaatti)
            peliin(syotit, siimat, tili)

    else:
        print("Osta kaupasta tarvikkeita. Ne on loppu :)")
        peliin(syotit, siimat, tili) 

    return syotit, siimat

def kauppa(tili, syotit, siimat):
    print("Valitse 1, jos haluat myydä kaikki kalat")
    print("Valitse 2, jos haluat ostaa siimaa")
    print("Valitse 3, jos haluat ostaa syöttejä")
    print("Valitse 4, jos haluat poistua kaupasta")

    valinta = input("Valitse 1, 2, 3 tai 4: ")

    print(f"Tilin saldo: {tili}€")

    if valinta == "1":
        tili = tili + reppu.repullisen_arvo()
        reppu.tyhjenna_reppu()
        print(f"Tilin saldo: {tili}€")
        peliin(syotit, siimat, tili)

    if tili > 50:
        if valinta == "2":
            siimat = siimat + 1
            tili = tili - 50
            print(f"Tilin saldo: {tili}€")
            print(f"Syötit: {syotit}")
            print(f"Siimat: {siimat}")
            peliin(syotit, siimat, tili)

        elif valinta == "3":
            syotit = syotit + 3
            tili = tili - 50
            print(f"Tilin saldo: {tili}€")
            print(f"Syötit: {syotit}")
            print(f"Siimat: {siimat}")
            peliin(syotit, siimat, tili)

        elif valinta == "4":
            peliin(syotit, siimat, tili)

    else: 
        print("Sulla ei oo rahaa, köyhä. Taisit hävitä pelin(muista myydä reppu ensin, että saat tilille rahulia)")
        paavalikko()
        
    return tili, syotit, siimat




def peliin(syotit, siimat, tili):

    while True:
        print("Valitse 1, jos haluat kalastaa")
        print("Valitse 2, jos tarkastaa repun sisällön")
        print("Valitse 3, jos haluat mennä kauppaan")
        print("Valitse 4, jos haluat mennä päävalikkoon")

        valinta = input("Valitse 1, 2, 3 tai 4: ")

        if valinta == "1":
            print("Aloitit kalastamisen")
            syotit, siimat = kalastaminen(syotit, siimat)
            break
        
        elif valinta == "2":
            print(reppu.merkkijonona())
            print(f"Syötit: {syotit}")
            print(f"Siimat: {siimat}")

        elif valinta == "3":
            print("Mennään kauppaan...")
            tili, syotit, siimat = kauppa(tili, syotit, siimat)
            break

        elif valinta == "4":
            print("Päävalikkoon...")
            paavalikko()
            break
           




def paavalikko():

    while True:
        
        print("Päävalikko")
        print("Valitse 1, jos haluat aloittaa kalastamisen")
        print("Valitse 2, jos haluat poistua pelistä")

        valinta = input("Valitse 1 tai 2: ")
        print(f"debug {valinta}")

        if valinta == "1":
            print("Siirrytään peliin....")
            peliin(syotit, siimat, tili)
            break


        elif valinta == "2":
            print("Poistutaan pelistä")
            print("Tulos:")
            print(reppu.merkkijonona())
            
            break

        else:
            print("Syötä numero 1, 2 tai 3!")


paavalikko()








