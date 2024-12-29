L = 3
C = 3
MAX = 1
MIN = 2
ZERO = 0



class Node:
    def __init__(self,grille=None,isMax=True):
        if grille == None:
            self.grille = [[ZERO for _ in range(L)] for _ in range(C)]
        else:  
            self.grille = grille
        
        self.isMax = isMax
        self.h = 0 # evaluation d'un node
        
    def __str__(self):
        chaine = "[\n"
        for line in range(L):
            for col in range(C):
                chaine += " " + str(self.grille[line][col])
            chaine += '\n'
        chaine += "]\n" + "H = " + str(self.h) +'\n' +" ScoreMAX: "+ str(self.getScore(MAX)) +" ScoreMIN: "+str(self.getScore(MIN))
        
        return chaine
    
    def pionsAligneLignes(self,pion):
        score = 0
        for i in range(L):
            line = self.grille[i]
            if line.count(pion) == 3:
                score += 10_000
            if line.count(pion) == 2 and line.count(ZERO) == 1:
                score += 200
            if line.count(pion) == 1 and line.count(ZERO) == 2:
                score += 30
            
        return score 
    
    def pionsAligneColones(self,pion):
        score = 0
        for i in range(C):
            col = [ligne[i] for ligne in self.grille]
            if col.count(pion) == 3:
                score += 10_000
            if col.count(pion) == 2 and col.count(ZERO) == 1:
                score += 200
            if col.count(pion) == 1 and col.count(ZERO) == 2:
                score += 30
            
        return score 
    
    def  pionsAligneDiagonales(self,pion):
        score = 0
        # Diagonale principale
        diagonale_principale = [self.grille[i][i] for i in range(L)]
        
        # Diagonale secondaire
        diagonale_secondaire = [self.grille[i][L - i - 1] for i in range(L)]
        
        diagonales = [diagonale_principale,diagonale_secondaire]
        for diagonale in diagonales:
            if diagonale.count(pion) == 3:
                score += 10_000
            if diagonale.count(pion) == 2 and diagonale.count(ZERO) == 1:
                score += 200
            if diagonale.count(pion) == 1 and diagonale.count(ZERO) == 2:
                score += 30
            
        return score 
    
    def getScore(self,pion):
        score = self.pionsAligneColones(pion) + self.pionsAligneDiagonales(pion) + self.pionsAligneLignes(pion)
        return score

    
    def updateHeuristique(self):
        self.h = self.getScore(MAX) - self.getScore(MIN)
        
    def gameEnd(self):
        if (self.pionsAligneLignes(MAX)>= 10_000 or
            self.pionsAligneLignes(MIN)>= 10_000 or
            self.pionsAligneColones(MAX)>= 10_000 or
            self.pionsAligneColones(MIN)>= 10_000 or
            self.pionsAligneDiagonales(MAX)>= 10_000 or
            self.pionsAligneDiagonales(MIN)>= 10_000
            ):
            return True
        return False
        



 
def main():
    grille = [
    [1, 2, 0],
    [0, 1, 0],
    [2, 2, 1]
    ]
    
    node = Node(grille)
    
    print(node)
    print(node.gameEnd())

    
    

if __name__ == "__main__":
    main()
    