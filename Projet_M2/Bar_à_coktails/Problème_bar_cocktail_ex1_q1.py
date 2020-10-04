import sys

class Accessoire(list):
    pass

class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    def embrocher(self,postit):
        self.append(postit)

    def liberer(self):
        postit = self.pop()
        return(postit)

class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    def recevoir(self,plateau):
        self.append(plateau)

    def evacuer(self):
        plateau = self.pop()
        return(plateau)

class Barman:

    def __init__(self,pic,bar):
        self.pic = pic
        self.bar = bar
        print('[Barman] Prêt pour le service !')

    def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        plateau = self.pic.liberer()
        for i in plateau :
            print(f'[Barman] Je commence la fabrication de {i}')
            print(f'[Barman] Je termine la fabrication de {i}')
        self.bar.recevoir(plateau)
        

class Serveur:

    def __init__(self,pic,bar,commandes):
        self.pic = pic
        self.bar = bar
        self.commandes = commandes
        print('[Serveur] Prêt pour le service')

    
    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        for commande in self.commandes:
            print(f'[Serveur] Je prends commande de {commande}')
        print("[Serveur] Il n'y a plus de commandes à prendre")
        self.pic.embrocher(self.commandes)


    def servir(self):
        """ Prend un plateau sur le bar. """
        commandes = self.bar.evacuer()
        for commande in commandes:
            print(f'[Serveur] Je sers {commande}')

  
#Programme principal

def main():
    try:
        serveur.prendre_commande()
    except Cocktail_Error as e:
        log(1,e)
    try:
        barman.preparer()
    except Cocktail_Error as e:
        log(1,e)
    try:
        serveur.servir()
    except Cocktail_Error as e:
        log(1,e)


if __name__ == '__main__':

    pic = Pic()
    bar = Bar()
    commandes = sys.argv[1:]
    barman = Barman(pic,bar)
    serveur = Serveur(pic,bar,commandes)
    main()
