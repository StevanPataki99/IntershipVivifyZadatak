import random

class Pica:
    def __init__(self, naziv, zapremina):
        self.naziv = naziv
        self.zapremina = zapremina
        self.cena = random.randrange(150,500)

    def dobavi_cenu(self):
        return self.cena