from LinkedList import LinkedList, Node

class OrderedLinkedList(LinkedList):

    def __init__(self, lst=[]):
        """
        Initialises a new ordered linked list object, with a given list of elements lst.
        @pre:  -
        @post: A new ordered linked list object has been initialised.
               Its length is equal to the number of elements in lst.
               The data elements stored in the linked list's nodes correspondent to those of the list lst,
               mais ils sont insérés de façon à respecter l'ordre défini par les comparaisons (<).
               Si aucune liste lst n'est donnée, la liste est vide.
        """
        super().__init__([])
        for elem in lst:
            self.add(elem)

    def size(self):
        """
        Accessor method which returns the number of nodes contained in this ordered linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this ordered linked list.
        """
        return self.length

    def add(self, cargo):
        """
        Adds a new Node with given cargo to the ordered linked list such that the order is maintained
        @pre:  self is a (possibly empty) OrderedLinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the ordered linked list in an ordered manner.
               The length counter has been incremented by 1.
        """
        new_node = Node(cargo)

        if self.first() is None:
            self.set_first(new_node)
            self.last = new_node
            self.inc_size()
            return

        first = self.first()

        if cargo <= first.value():
            new_node.set_next(first)
            self.set_first(new_node)
            self.inc_size()
            return

        prev = first
        cur = first.next()

        while cur is not None and cur.value() <= cargo:
            prev = cur
            cur = cur.next()

        new_node.set_next(cur)
        prev.set_next(new_node)

        if cur is None:
            self.last = new_node

        self.inc_size()

    def remove(self, cargo):
        """
        Removes the first node with a given cargo from the list.
        Leaves the list intact if already empty or if a node with that cargo
        doesn't exist.
        """
        if self.first() != None:

            head = self.first()


            if head.value() == cargo:
                self.set_first(head.next())
                self.dec_size()
                if self.size() == 0:
                    self.last = None
                return

            prev = head
            cur = head.next()

            while cur is not None and cur.value() != cargo:
                prev = cur
                cur = cur.next()

            if cur is not None:
                prev.set_next(cur.next())
                self.dec_size()
                if cur.next() is None:
                    self.last = prev
