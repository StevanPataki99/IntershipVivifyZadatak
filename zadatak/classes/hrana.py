import random
from classes.prilog import Prilog

class Hrana:
    def __init__(self, naziv, prilozi = []):
        self.naziv = naziv
        self.cena = random.randrange(300,600)
        self.prilozi = prilozi

    def dobavi_cenu(self):
        ukupna_cena = self.cena
        for prilog in self.prilozi:
            ukupna_cena += prilog.dobavi_cenu()
        
        return ukupna_cena