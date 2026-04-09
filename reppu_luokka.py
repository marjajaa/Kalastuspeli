
class Reppu:

    def __init__(self):
        self.sisalto = []

    def lisaa(self, kala):
        self.sisalto.append(kala)

    def repullisen_arvo(self):
        return sum(kala.arvo() for kala in self.sisalto)



    def merkkijonona(self):
        print("Repun sisältö:")
        for kala in self.sisalto:
            print(kala)
        print(f"Yhteensä: {self.repullisen_arvo()}€ ")

    def __str__(self):
        return self.merkkijonona()
        