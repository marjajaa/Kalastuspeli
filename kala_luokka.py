import math


hinnat = {
    "kuha": 12,
    "ahven": 8,
    "taimen": 14,
    "lohi": 15,
    "hauki": 6,
    "siika": 10
}


class Kala:
    def __init__(self, kalalaji, paino):
        self.kalalaji = kalalaji
        self.paino = paino
        self.hinta_per_kg = hinnat[kalalaji]

    def arvo(self):
        return round(self.paino * self.hinta_per_kg, 2)

    def __str__(self):
        return f"{self.kalalaji} {self.paino}kg ({self.arvo()}€)"