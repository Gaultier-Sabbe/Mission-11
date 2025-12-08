from Duree import Duree

class ListeLecture:
    class Node:
        def __init__(self,data,next=None):
            self.data = data
            self.next = next
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
        self.duree = Duree(0, 0, 0)
        self.__head = None
        self.__length = 0

    def ajouter(self, media):
        """
        Ajoute 'media' à la liste de lecture
        @pre: media est une instance de 'Media'
        @post: la liste de lecture comprend maintenant 'media'
        """
        self.__head = self.Node(media,self.__head)
        self.__length += 1
        self.duree.ajouter(media.duree)

    def retirer(self, media):
        """
        Retire 'media' à la liste de lecture
        @pre: media est une instance de 'Media'
        @post: la liste de lecture ne contient plus 'media'
        """
        if self.__head != None:
            done = False
            if self.__head.data == media:
                self.__head == self.__head.next
                done = True
            else:
                cur = self.__head
                while cur.next is not None and cur.next.data != media:
                    if cur.next.data == media:
                        cur.next = cur.next.next
                        done = True
                    cur = cur.next
            if done:
                self.__length -= 1



    def nombre_de_medias(self):
        """Renvoie le nombre de medias dans liste"""
        return self.__length

    def __str__(self):
        s = "[#{}] {} ({} medias)\n".format(self.id,self.name,self.nombre_de_medias())
        #s = f"[#{self.id}] {self.name} ({len(self.medias)} medias)\n"
        cur = self.__head
        i = 0
        while cur.next is not None:
            s += "{:02}: ".format(i) + str(cur.data) + "\n"
            i += 1
            cur = cur.next
        return s[:-1]  # return s sans le dernier "\n"
