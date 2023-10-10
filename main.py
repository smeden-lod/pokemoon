"""
Le module principal
"""
from pokemoon import Pokemoon

class Jeu :

    def __init__(self,x: Pokemoon, y: Pokemoon):
        self.c1 = x
        self.c2 = y
        self.gagnant = None

    def run(self): #code du combat
        x = self.c1
        y = self.c2
        while self.c1.alive and self.c2.alive:
            x.fight(y)
            x, y = y, x
        if not self.c1.alive:
            self.gagnant = self.c2
        else: 
            self.gagnant = self.c1
        print(f"{self.gagnant.nom} gagne")



c1 = Pokemoon("salamèche", 30, True, False, False) #Tous les différents Pokemoons
c2 = Pokemoon("Darumarond", 30, True, False, False)
c3 = Pokemoon("Carapuce", 30, False, True, False)
c4 = Pokemoon("Moustillon", 30, False, True, False)
c5 = Pokemoon("Bulbizzare", 30, False, False, True)
c6 = Pokemoon("Vipélierre", 30, False, False, True)

# choix1 = int(input('c1, c2, c3, c4, c5, c6'))

j= Jeu(c6,c3) #choix du Pokemoon

j.run()
