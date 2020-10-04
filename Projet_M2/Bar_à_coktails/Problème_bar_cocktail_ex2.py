import sys
import asyncio

class Accessoire(list):
    pass

class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. (le postit représentant une commande à chaque fois contrairement 
        à la question précédente) """

    async def embrocher(self,commande):
        await asyncio.sleep(0.01)
        print(f'[Pic] postit {commande} embroché')
        self.append(commande)

    async def liberer(self, postit):
        await asyncio.sleep(0.01)
        print(f'[Pic] postit {postit} libéré')
        #return(self)

class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    async def recevoir(self,plateau):
        await asyncio.sleep(0.01)
        print(f'[Bar] {plateau} reçu')
        self.append(plateau)

    async def evacuer(self,commande):
        await asyncio.sleep(0.01)
        print(f'[Bar] {commande} évacuée')
        #return(self)

class Barman:

    def __init__(self,pic,bar):
        self.pic = pic
        self.bar = bar
        print('[Barman] Prêt pour le service !')

    async def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        plateau = self.pic
        for i in plateau :
            await self.pic.liberer(i)
            print(f'[Barman] Je commence la fabrication de {i}')
            await asyncio.sleep(0.5)
            print(f'[Barman] Je termine la fabrication de {i}')
            await self.bar.recevoir(i)
            
        

class Serveur:

    def __init__(self,pic,bar,commandes):
        self.pic = pic
        self.bar = bar
        self.commandes = commandes
        print('[Serveur] Prêt pour le service')

    
    async def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        for commande in self.commandes:
            await asyncio.sleep(1)
            print(f'[Serveur] Je prends commande de {commande}')
            await self.pic.embrocher(commande)
        print("[Serveur] Il n'y a plus de commandes à prendre")
       


    async def servir(self):
        """ Prend un plateau sur le bar. """
        commandes = self.bar
        for commande in commandes:
            #await asyncio.sleep(0.01)
            await self.bar.evacuer(commande)
            await asyncio.sleep(0.01)
            print(f'[Serveur] Je sers {commande}')

  
#Programme principal

async def main_prog():
    await asyncio.gather(
    serveur.prendre_commande(),
    barman.preparer(),
    serveur.servir()
    )
        


if __name__ == '__main__':

    pic = Pic()
    bar = Bar()
    commandes = sys.argv[1:]
    barman = Barman(pic,bar)
    serveur = Serveur(pic,bar,commandes)
    asyncio.run(main_prog())
