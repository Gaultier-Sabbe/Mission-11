from Duree import Duree
from OrderedLinkedList import OrderedLinkedList

class ListeLecture(OrderedLinkedList):

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.duree = Duree(0, 0, 0)
        self.__medias = OrderedLinkedList()

    def ajouter(self, media):

        self.__medias.add(media)
        self.duree.ajouter(media.duree)

    def retirer(self, media):
        if self.__medias.first() != None:
            head = self.__medias.first()

            if head.value() == media:
                self.__medias.set_first(head.next())
                self.__medias.dec_size()
                if self.__medias.size() == 0:
                    self.__medias.last = None
                return

            cur = head
            while cur.next() is not None and cur.next().value() != media:
                cur = cur.next()

            if cur.next() is not None and cur.next().value() == media:
                to_remove = cur.next()
                cur.set_next(to_remove.next())
                self.__medias.dec_size()

                if cur.next() is None:
                    self.__medias.last = cur

    def nombre_de_medias(self):
        return self.__medias.size()

    def __str__(self):
        
        s = "[#{}] {} ({} medias)\n".format(self.id, self.name, self.nombre_de_medias())
        i = 0
        current = self.__medias.first()

        while current is not None:
            s += "{:02}: ".format(i) + str(current.value()) + "\n"
            current = current.next()
            i += 1

        if i > 0:
            return s[:-1]
        return s

