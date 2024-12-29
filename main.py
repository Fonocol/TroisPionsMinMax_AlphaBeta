from Node import Node, ZERO,C,L,MAX,MIN
from TroisPions import TroisPions
PROFONDEUR = 3
NOMBREPION = 3


def startGame():
    game = TroisPions()
    print(game)
    finJeu = False
    positionement = True
    while (not finJeu):
        
        # TODO pose pion    
        
        if positionement == True:
            print("debut de la phase de positionement :")
            for i in range(NOMBREPION):
                x,y = map(int,input("Jouer une colonne 0-2 et une ligne 0-2 :").split())
                while not (0 <= x < L) or not (0 <= y < C) or game.grillejeu[x][y] != ZERO :
                    x,y = map(int,input("Jouer une colonne 0-2 et une ligne 0-2 :").split())
                
                game.posePion(MIN,x,y,game.grillejeu)
                print(game)
                initialNode = Node(grille=game.grillejeu,isMax=True)
                if(initialNode.gameEnd()):
                    print(" Vous avez gagné  !\n")
                    finJeu = True
                    break
                else:
                    eval,bestx,besty,besta,bestb= game.alpha_beta_max_min(initialNode,float('-inf'),  float('inf'),profondeur=PROFONDEUR)
                    game.posePion(MAX,bestx,besty,game.grillejeu)
                    print(game)
                    print(f" IA a joué la position {bestx} {besty}")
                    initialNode = Node(grille=game.grillejeu,isMax= False)
                    if(initialNode.gameEnd()):
                        print("L'IA a gagné  !\n")
                        finJeu = True
                        break
            print("fin de la phase de positionement :")
            positionement = False
        
        else:           
            #TODO logique de deplacement
            x,y,a,b = map(int,input("deplacement de (x,y) vers (a,b):").split())
            while  game.deplacerPion(MIN,x,y,a,b, game.grillejeu) == False:
                x,y,a,b = map(int,input("deplacement de (x,y) vers (a,b):").split())

            print(game)
            initialNode = Node(grille=game.grillejeu,isMax=True)
            if(initialNode.gameEnd()):
                print(" Vous avez gagné  !\n")
                finJeu = True
            else:
                eval,bestx,besty,besta,bestb = game.alpha_beta_max_min(initialNode,float('-inf'),  float('inf'),phase="deplacement",profondeur=PROFONDEUR)
                game.deplacerPion(MAX,bestx,besty,besta,bestb, game.grillejeu)
                print(game)
                print(f" IA a deplacer de  {bestx} {besty} vers {besta} {bestb}")
                initialNode = Node(grille=game.grillejeu,isMax= False)
                if(initialNode.gameEnd()):
                    print("L'IA a gagné  !\n")
                    finJeu = True
                  
        
        
if __name__ == "__main__":
    startGame()
    
  