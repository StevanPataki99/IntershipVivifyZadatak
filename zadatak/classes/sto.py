from classes.porudzbina import Porudzbina
from classes.nije_naplaceno import NijeNaplaceno

class Sto:
    def __init__(self, broj):
        self.broj = broj
        self.porudzbina = None

    def poruci(self, porudzbina):
        try:
            if self.porudzbina != None:
                raise NijeNaplaceno
            else:
                self.porudzbina = porudzbina
                self.porudzbina.poruci()
        except NijeNaplaceno:
            print("Nije moguće izdati novu porudžbinu jer prethodna nije plaćena.")

    def naplati(self):
        if self.porudzbina == None:
            print("Sto je prazan")
        else:
            self.porudzbina.naplati()
            self.porudzbina = None
