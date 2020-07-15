from classes.sto import Sto
from classes.porudzbina import Porudzbina
from classes.pizza import Pizza
from classes.pasta import Pasta
from classes.negazirani_sokovi import NegaziraniSokovi
from classes.gazirani_sokov import GaziraniSokovi
from classes.voda import Voda
from classes.prilog import Prilog

sto1 = Sto(1)
sto2 = Sto(2)
sto3 = Sto(3)
sto4 = Sto(4)

prilog_kecap = Prilog("kecap")
prilog_origano = Prilog("origano")
prilog_cheese = Prilog("extra cheese")
prilog_parmezan = Prilog("parmezan")
prilog_biber = Prilog("biber")

pizza1 = Pizza("Capricciosa", [prilog_kecap, prilog_origano])
pizza2 = Pizza("Capricciosa", [prilog_kecap, prilog_kecap])
pizza3 = Pizza("Siciliana", [])
pizza4 = Pizza("Margarita", [])

pasta1 = Pasta("Italiana", [prilog_cheese])
pasta2 = Pasta("Carbonara", [])
pasta3 = Pasta("Carbonara", [prilog_parmezan])
pasta4 = Pasta("Italiana", [])
pasta5 = Pasta("Bolonjez", [])

pice1 = GaziraniSokovi("Coca Cola", 0.5)
pice2 = NegaziraniSokovi("Narandza", 0.25)
pice3 = Voda("Voda", 0.5)
pice4 = GaziraniSokovi("Pepsi", 0.3)
pice5 = NegaziraniSokovi("Jabuka", 0.5)

Porudzbina1 = Porudzbina(sto1, [pizza1, pasta1, pice2])
Porudzbina2 = Porudzbina(sto2, [pizza3, pasta2, pice1, pice1])
Porudzbina3 = Porudzbina(sto3, [pizza2, pizza2, pizza2, pice4, pice5, pice3])
Porudzbina4 = Porudzbina(sto2, [pizza2]) 

sto1.poruci(Porudzbina1)
sto2.poruci(Porudzbina2)
sto3.poruci(Porudzbina3)

sto1.naplati()
sto3.naplati()

sto2.poruci(Porudzbina4)

sto2.naplati()

sto2.poruci(Porudzbina4)
