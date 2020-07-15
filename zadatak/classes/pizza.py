from classes.hrana import Hrana

class Pizza(Hrana):
    def __init__(self, naziv, prilozi = []):
        super().__init__(naziv, prilozi)
