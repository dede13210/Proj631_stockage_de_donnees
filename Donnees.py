import itertools


class Donnees:
    newid = itertools.count()

    def __init__(self, t):
        self.id = next(Donnees.newid)
        self.taille = t
