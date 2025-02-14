import numpy

class Grille:
    """longueur = 0
    hauteur = 0
    grille =[0]
    derniercoup = [0,0]"""
    def __init__(self,hauteur, longueur):
        """self.longueur = longueur
        self.hauteur = hauteur"""
        self.grille = numpy.zeros(hauteur, longueur)
        
    def coup(self, joueur, colonne):
        if (colonne > self.longueur-1) and (colonne <0):
            return 1
        for i in range(self.hauteur, -1, -1):
            if self.grille[i][colonne] == 0:
                self.grille[i][colonne] = joueur
                self.derniercoup = [i, colonne]
                return 0
        return 2
        
    def test_rempli(self):
        if 0 in self.grille:
            return False
        else:
            return True
        
    def test_fin(self):
        y = self.derniercoup[0]
        x = self.derniercoup[1]
        joueur = self.grille[y][x]
        i = x
        #test ligne horizontale
        
        #recherche début de ligne
        while(self.grille[y][i] == joueur) and (i >=0):
            i-=1
        i+=1

        #test distance à la fin de la grille
        ligne = False
        if i+4 > self.largeur:
            ligne = False
        else:
            #test 4 jetons alignés
            ligne = True
            for a in range(0,4):
                if self.grille[y][i+a] != joueur:
                    ligne = False
        
        if ligne : 
            return True
        
        #test ligne verticale
        i=y
        
        #recherche début de ligne
        while(self.grille[i][x] == joueur) and (i >=0):
            i-=1
        i+=1
        #test distance à la fin de la grille
        ligne = False
        if i+4 > self.hauteur:
            ligne = False
        else:
            #test 4 jetons alignés
            ligne = True
            for a in range(0,4):
                if self.grille[i+a][x] != joueur:
                    ligne = False
        if ligne:
            return True
        
        #test diagonale gauche
        i = y
        j = x
        
        #recherche début de ligne
        while(self.grille[i][j] == joueur) and (i >=0) and (j >=0):
            i-=1
            j-=1

        i+=1
        j+=1

        #test distance à la fin de la grille
        ligne = False
        if (i+4 > self.hauteur) or (j+4> self.largeur):
            ligne = False
        else:
            #test 4 jetons alignés
            ligne = True
            for a in range(0,4):
                if self.grille[i+a][j+a] != joueur:
                    ligne = False
        if ligne:
            return True
        
        #test diagonale droite
        i = y
        j = x
        
        #recherche début de ligne
        while(self.grille[i][j] == joueur) and (i >=0) and (j >=0):
            i+=1
            j-=1

        i-=1
        j+=1

        #test distance à la fin de la grille
        ligne = False
        if (i-4 < 0) or (j+4> self.largeur):
            ligne = False
        else:
            #test 4 jetons alignés
            ligne = True
            for a in range(0,4):
                if self.grille[i-a][j+a] != joueur:
                    ligne = False
        if ligne:
            return True
        
        #tests ratés on return False
        return False
