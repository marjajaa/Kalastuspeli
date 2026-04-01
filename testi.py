 #kalalajit = ["kuha", "ahven", "taimen", "lohi", "hauki", "siika"]


def peliin():
    print("Päästiin peliin")

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

    print(f"debug {valinta}")

paavalikko()








