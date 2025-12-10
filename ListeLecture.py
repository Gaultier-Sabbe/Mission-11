from Duree import Duree
from LinkedList import LinkedList
from OrderedLinkedList import OrderedLinkedList

class ListeLecture:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.duree = Duree(0, 0, 0)
        self.medias = LinkedList()

    """
    Ajoute 'media' à la liste de lecture
    @pre:  media est une instance de 'Media'
    @post: la liste de lecture comprend maintenant 'media'
    """
    def ajouter(self, media):

        self.medias.add(media)
        self.duree.ajouter(media.duree)

    """
    Retire 'media' la première occurence de 'media' à la liste de lecture
    @pre:  media est une instance de 'Media'
    @post: la première instance de 'media' dans la liste de lecture
           a été supprimé
    """
    def retirer(self, media):
        if self.medias.first() != None:
            head = self.medias.first()

            if head.value() == media:
                self.medias.set_first(head.next())
                self.medias.dec_size()
                if self.medias.size() == 0:
                    self.medias.last = None
                return

            cur = head
            while cur.next() is not None and cur.next().value() != media:
                cur = cur.next()

            if cur.next() is not None and cur.next().value() == media:
                to_remove = cur.next()
                cur.set_next(to_remove.next())
                self.medias.dec_size()

                if cur.next() is None:
                    self.medias.last = cur

    """Renvoie le nombre de medias dans liste"""
    def nombre_de_medias(self):
        return self.medias.size()

    """
    Renvoie un string avec une description de la liste
    et tous ses éléments.
    """
    def __str__(self):
        
        s = "[#{}] {} ({} medias)\n".format(self.id, self.name, self.nombre_de_medias())
        i = 0
        current = self.medias.first()

        while current is not None:
            s += "{:02}: ".format(i) + str(current.value()) + "\n"
            current = current.next()
            i += 1

        if i > 0:
            return s[:-1]
        return s

class ListeLectureOrdonnee(ListeLecture):
    """
    @pre:  name est un string
           id est un entier
    @post: une instance de 'ListeLecture' ayant un identifiant unique.
    """
    def __init__(self, name, id) :
        super().__init__(name, id)
        self.medias = OrderedLinkedList()