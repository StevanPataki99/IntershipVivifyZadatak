import random

class Prilog():
    def __init__(self, naziv):
        self.naziv = naziv
        self.cena = random.randrange(20,100)

    def dobavi_cenu(self):
        return self.cena