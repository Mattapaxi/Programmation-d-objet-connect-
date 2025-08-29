import operator

class Compteur():
    def __init__(self, texte):
        self.texte = texte
    
    def compter_les_mots(self):
        mots = self.texte.split()
        compter_des_mots = {}
        for mot in mots:
            if mot not in compter_des_mots:
                compter_des_mots[mot]=1
            else:
                compter_des_mots[mot]+=1
        mots_tries = sorted(compter_des_mots.items(), key=operator.itemgetter(1), reverse = True)
        print(mots_tries)
        