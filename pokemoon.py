"""
dans ce module on définit le pokemoon
"""
from type_poke import efficacite, eau, feu, plante 

class Pokemoon:

    def __init__(self, n: str, pv: int, type_feu: bool, type_eau: bool, type_plante: bool) -> None:
        self.nom = n
        self.pv = pv # nombre de pv du pokémon
        self.alive = True # True si tj en vie et inversement 
        self.p = 2 # potions
        self.sp = 1
        self.type = type_feu, type_eau, type_plante
        self.type_feu = type_feu
        self.type_eau = type_eau
        self.type_plante = type_plante

    def fight(self, other):
        input(f"Au tour de {self.nom}")
        action = int(input("coup d'boule(1) , charge(2) , sac(3)  "))# attaque spécifique au type(2)
        if action == 1 :
            other.pv -=8
        if action == 2 :
            if efficacite[(self.type,other.type)]:
                other.pv -= 30
                print("super efficace")
            else :
                    other.pv -= 20
        if action == 3 :
            soins = int(input("potion(1) , super potion(2)  "))# ça s'apelle tj soins mais c'est les potions 
            if soins == 1 : 
                    if self.p >= 1 :
                        self.pv += 6
                        s = 6
                        self.p -= 1 # nombre limiter de potion 
                        print(f"{self.nom}, {self.pv} (+{s})")
                    else : 
                        print("vous n'avez plus de potions")
            if soins == 2 : 
                    if self.sp >= 1:
                        self.pv += 10
                        s = 10
                        self.sp -= 1
                        print(f"{self.nom}, {self.pv} (+{s})")
                    else :
                        print("vous n'avez plus de super potions")
        if other.pv <= 0 :
            other.alive = False
