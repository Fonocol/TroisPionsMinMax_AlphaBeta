from copy import deepcopy
from Node import Node, ZERO,C,L,MAX,MIN



class TroisPions:
    def __init__(self,grillejeu=None):
        self.grillejeu = [[ZERO for _ in range(C)] for _ in range(L)]
        #self.grillejeu = grillejeu
    
    def __str__(self):
        symboles = {
            ZERO: "⚫", 
            MAX: "🔴",   
            MIN: "⚪"    
        }

        chaine = "    " 
        for j in range(C):
            chaine += f"{j}    "  # Indices de colonnes
        chaine += "\n  +" + "----+" * C + "\n"  # Ligne supérieure de la bordure

        for i in range(L):
            chaine += f"{i} |"  # Indice de la ligne
            for j in range(C):
                valeur = self.grillejeu[i][j]
                chaine += f" {symboles[valeur]} |"  
            chaine += "\n  +" + "----+" * C + "\n" 

        return chaine
    
    def posePion(self,pion,x,y,grille):
        if 0<= x <L and 0<=y<C:
            if grille[x][y] == ZERO:
                grille[x][y] = pion
                return True
            
        return False
    
    def deplacerPion(self, pion, x, y, a, b, grille):

        if not (0 <= x < L and 0 <= y < C and 0 <= a < L and 0 <= b < C):
            return False
        
        if not (x - 1 <= a <= x + 1) or not (y - 1 <= b <= y + 1):
            return False

        if (x==1 and y==1) or (x==0 and y==0) or (x==L-1 and y==C-1) or (x==0 and y==C-1) or (x==L-1 and y==0):
            if grille[x][y] == pion and grille[a][b] == ZERO:
                grille[x][y] = ZERO
                self.posePion(pion, a, b, grille)
                return True
        else:
            #deplacement des pion au cote au milieux
            if (a== x-1 and b== y-1) or (a== x+1 and b== y+1) or (a== x+1 and b== y-1) or (a== x-1 and b== y+1):
                return False
            else:
                if grille[x][y] == pion and grille[a][b] == ZERO:
                    grille[x][y] = ZERO
                    self.posePion(pion, a, b, grille)
                    return True
        return False
    
    def alpha_beta_max_min(self,node:Node,alpha,beta,phase='deposePion',profondeur=3):
        if profondeur == 0 or node.gameEnd():
            node.updateHeuristique()
            return (node.h,-1,-1,-1,-1)
        
        bestx,besty = -1,-1
        besta,bestb = -1,-1
        if node.isMax:
            max_eval = float('-inf')
            for x in range(L):
                for y in range(C):
                    if phase == 'deposePion':
                        grillCopy = deepcopy(node.grille)
                        is_valid = self.posePion(MAX,x,y,grillCopy)
                        if is_valid:
                            s = Node(grillCopy,False)
                            eval, _, _ ,_,_= self.alpha_beta_max_min(s,alpha,beta,phase,profondeur =profondeur-1)
                            if eval> max_eval:
                                max_eval = eval
                                bestx,besty = x,y
                            alpha = max(alpha,eval)
                            if alpha >= beta:
                                break
                    else:
                        for a in range(x-1,x-1+L):
                            for b in range(y-1,y-1+C):
                                grillCopy = deepcopy(node.grille)
                                is_valid = self.deplacerPion(MAX,x,y,a,b,grillCopy)
                                if is_valid:
                                    s = Node(grillCopy,False)
                                    eval, _, _ ,_,_= self.alpha_beta_max_min(s,alpha,beta,phase,profondeur =profondeur-1)
                                    if eval> max_eval:
                                        max_eval = eval
                                        bestx,besty = x,y
                                        besta,bestb = a,b
                                    alpha = max(alpha,eval)
                                    if alpha >= beta:
                                        break                         
            return (max_eval,bestx,besty,besta,bestb)
                    
        else:
            min_eval = float('inf')
            for x in range(L):
                for y in range(C):
                    if phase == 'deposePion':
                        grillCopy = deepcopy(node.grille)
                        is_valid = self.posePion(MIN,x,y,grillCopy)
                        if is_valid:
                            s = Node(grillCopy,True)
                            eval, _, _,_,_ = self.alpha_beta_max_min(s,alpha,beta,phase,profondeur =profondeur-1)
                            if eval < min_eval:
                                min_eval = eval
                                bestx,besty = x,y
                            beta = min(beta,eval)
                            if alpha >= beta:
                                break    
                    else:
                        for a in range(x-1,x-1+L):
                            for b in range(y-1,y-1+C):
                                grillCopy = deepcopy(node.grille)
                                is_valid = self.deplacerPion(MIN,x,y,a,b,grillCopy)
                                if is_valid:
                                    s = Node(grillCopy,False)
                                    eval, _, _ ,_,_= self.alpha_beta_max_min(s,alpha,beta,phase,profondeur =profondeur-1)
                                    if eval < min_eval:
                                        min_eval = eval
                                        bestx,besty = x,y
                                        besta,bestb = a,b
                                    beta = min(beta,eval)
                                    if alpha >= beta:
                                        break                          
            return (min_eval,bestx,besty,besta,bestb)




def main():
    grille = [
    [1, 2, 0],
    [0, 1, 0],
    [2, 2, 1]
    ]
    
    node = Node()
    game = TroisPions(grille)
    
    
    print(game)
    print(node.gameEnd())
    game.deplacerPion(MAX, 2, 2, 0, 2, grille)
    game.deplacerPion(MAX, 1, 1, 1, 2, grille)
    game.deplacerPion(MAX, 0, 0, 3, 3, grille)
    game.deplacerPion(MAX, 0, 0, 1, 1, grille)
        
    print(game)
    
    
if __name__ == "__main__":
    main()