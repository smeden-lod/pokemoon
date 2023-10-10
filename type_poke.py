feu = True, False, False
eau = False, True, False
plante = False, False, True
efficacite = {
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
