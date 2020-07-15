
from classes.pica import Pica
from classes.hrana import Hrana
from datetime import datetime

class Porudzbina:
    def __init__(self, broj_stola, porucene_stavke = []):
        self.broj_stola = broj_stola
        self.porucene_stavke = porucene_stavke
        self.ukupna_cena = 0
        for stavka in self.porucene_stavke:
            self.ukupna_cena += stavka.dobavi_cenu()
        

    def naplati(self):
        print("Racun: datum {} sto broj {}, naplata {}rsd".format(datetime.now(), self.broj_stola, self.ukupna_cena))

    def poruci(self):
        print("Porudzbina: datum{} sto broj {}".format(datetime.now(), self.broj_stola))