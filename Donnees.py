<<<<<<< HEAD
import itertools


class Donnees:
    newid = itertools.count()

    def __init__(self, t):
        self.id = next(Donnees.newid)
        self.taille = t
=======
class Donnees:
   def __init__(self,i,t):
       self.id = i
       self.taille = t
>>>>>>> c33a323 (start)
