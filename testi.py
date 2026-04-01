 #kalalajit = ["kuha", "ahven", "taimen", "lohi", "hauki", "siika"]

#def kalastaminen():
#kalastuksen toiminnallisuus

#def reppu():
#mitä repussa on 

def peliin():
    print("Päästiin peliin")

    while True:
        print("Päästiin peliin")
        print("Valitse 1, jos haluat kalastaa")
        print("Valitse 2, jos tarkastaa repun sisällön")
    #repussa on kalat ja syötit


def paavalikko():

    while True:
        
        print("Päävalikko")
        print("Valitse 1, jos haluat aloittaa kalastamisen")
        print("Valitse 2, jos haluat poistua pelistä")

        valinta = input("Valitse 1 tai 2: ")
        print(f"debug {valinta}")

        if valinta == "1":
            print("Siirrytään peliin....")
            peliin()
            break


        elif valinta == "2":
            print("Poistutaan valikosta")
            break

        else:
            print("Syötä numero 1 tai 2!")


paavalikko()








