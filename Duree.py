class Duree :
    """Représente une durée en format hh:mm:ss"""

    def __init__(self, h, m, s):
        """
        @pre:
            - h est un entier positif.
            - m est un entier entre 0 (compris) et 60 (non compris)
            - s est un entier entre 0 (compris) et 60 (non compris)
        @post: Une object de type 'Duree' est créé
        """
        self.h = h
        self.m = m
        self.s = s

    def to_secondes(self):
        """Renvoie la durée en secondes"""
        return self.h*3600 + self.m*60 + self.s

    def delta(self, d):
        """
        Renvoie la différence en secondes entre 'self' et 'd'. Peut être négative si la durée représentée par 'd' est plus grande que celle de 'self'.
        @pre: d est une instance de 'Duree'
        @post: la différence en secondes entre 'self' et 'd'
        """
        return self.to_secondes()-d.to_secondes()

    def apres(self, d):
        """
        Renvoie l'ordre entre 2 durées
        @pre: d est une instance de 'Duree'
        @post: renvoie 'True' si la durée représentée par 'self' est strictement plus grande que celle représentée par 'd', renvoie 'False' sinon.
        """
        return self.delta(d) > 0

    def ajouter(self, d):
        """
        Ajoute la durée 'd' à 'self'.
        @pre: d est une instance de 'Duree'
        @post: la durée représentée par 'self' est incrémentée par la durée représentée par 'd'
        """
        sum = self.to_secondes()+d.to_secondes()
        self.s = sum%60
        self.m = sum//60 % 60
        self.h = sum//3600

    def __str__(self):
        """
        Revoie la représentation en string de la durée en format 'hh:mm:ss'
        """
        return "{:02}:{:02}:{:02}".format(self.h, self.m, self.s)
