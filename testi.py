 #kalalajit = ["kuha", "ahven", "taimen", "lohi", "hauki", "siika"]


def paavalikko():

    while True:
        print("kakka")
        print("Päävalikko")
        print("Valitse 1, jos haluat aloittaa kalastamisen")
        print("Valitse 2, jos haluat poistua pelistä")

        valinta = input("Valitse 1 tai 2: ")
        print(f"debug {valinta}")

        if valinta == "1":
            print("Aloitit pelin")
            
                

        elif valinta == "2":
            break

        else:
            print("Syötä numero 1 tai 2!")

    print(f"debug {valinta}")


paavalikko()






