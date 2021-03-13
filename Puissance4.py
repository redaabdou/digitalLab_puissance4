from Grille import *
class puissance4:

    """self.grille
    self.vainqueur = 0"""

def debut(self):
    hauteur = input("Entrez hauteur")
    while(hauteur < 4) and (type(hauteur) != int) :
        hauteur = input("Mauvaise valeure, choisir une hauteur supérieure à 4")
    
    largeur = input("Entrez largeur")
    while(largeur < 4) and (type(largeur) != int) :
        largeur = input("Mauvaise valeure, choisir une largeur supérieure à 4")
        
    self.grille = Grille(hauteur, largeur)
    partie()

def partie(self):
    joueur = 1
    continuer = True
    while( continuer ):
        colonne = input("Joueur "+joueur+" entrez votre prochain coup")
        valide = self.coup(joueur, colonne)
        while(valide != 0):
            if valide == 1:
                print("Mauvaise valeure")
            if valide == 2:
                print("Colonne pleine")
            colonne = input("Joueur "+joueur+" rejouez votre coup")
            valide = self.coup(joueur, colonne)

        if self.grille.test_rempli() :
            continuer = False
        elif self.grille.test_fin() :
            self.vainqueur = joueur
            continuer = False
            
        joueur = joueur % 2 + 1
        
    fin()

def fin(self):
    if self.vainqueur == 0:
        print("Match nul")
    else:
        print("Joueur " + self.vainqueur +" a gagné !")