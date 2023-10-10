class Pokémoon :
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
        feu = True, False, False
        eau = False, True, False
        plante = False, False, True
        éfficatité = {
        (feu , plante) : True, #renvoie True si il y a éfficacité de type sinon     False
        (feu , eau) : False,
        (feu , feu) : False,
        (plante , plante) : False,
        (plante , eau) : True,
        (plante , feu) : False,
        (eau , plante) : False,
        (eau , eau) : False,
        (eau , feu) : True
        }
        input(f"Au tour de {self.nom}")
        action = int(input("coup d'boule(1) , charge(2) , sac(3)  "))# attaque spécifique au type(2)
        if action == 1 :
            other.pv -=8
        if action == 2 :
            if éfficatité[(self.type,other.type)]:
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
               
class Jeu :

    def __init__(self,c1: Pokémoon,c2: Pokémoon):
        self.c1 = c1
        self.c2 = c2
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



c1 = Pokémoon("salamèche", 30, True, False, False) #Tous les différents pokémoons
c2 = Pokémoon("Darumarond", 30, True, False, False)
c3 = Pokémoon("Carapuce", 30, False, True, False)
c4 = Pokémoon("Moustillon", 30, False, True, False)
c5 = Pokémoon("Bublizzare", 30, False, False, True)
c6 = Pokémoon("Vipélierre", 30, False, False, True)

# choix1 = int(input('c1, c2, c3, c4, c5, c6'))

j= Jeu(c6,c3) #choix du pokémoon

j.run()