from Duree import Duree

class ListeLecture:
    """Une compilation de médias"""

    def __init__(self, name, id):
        """
        @pre:
            - name est un string
            - id est un entier
        @post: une instance de 'ListeLecture' ayant un identifiant unique.
        """
        self.name = name
        self.id = id
        self.medias = []
        self.duree = Duree(0, 0, 0)

    def ajouter(self, media):
        """
        Ajoute 'media' à la liste de lecture
        @pre: media est une instance de 'Media'
        @post: la liste de lecture comprend maintenant 'media'
        """
        self.medias.append(media)
        self.duree.ajouter(media.duree)

    def retirer(self, media):
        """
        Retire 'media' à la liste de lecture
        @pre: media est une instance de 'Media'
        @post: la liste de lecture ne contient plus 'media'
        """
        self.medias.remove(media)

    def nombre_de_medias(self):
        """Renvoie le nombre de medias dans liste"""
        return len(self.medias)

    def __str__(self):
        s = "[#{}] {} ({} medias)\n".format(self.id,self.name,len(self.medias))
        #s = f"[#{self.id}] {self.name} ({len(self.medias)} medias)\n"
        i = 1
        for media in self.medias:
            s += "{:02}: ".format(i) + str(media) + "\n"
            i += 1
        return s[:-1]  # return s sans le dernier "\n"
