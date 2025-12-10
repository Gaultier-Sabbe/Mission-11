####################
# LinkedList class #
####################

class LinkedList :
    
    def __init__(self, lst=[]):
        """
        Initialises a new linked list object, with a given list of elements lst.
        @pre:  -
        @post: A new linked list object has been initialised.
               Its length is equal to the number of elements in lst.
               The data elements stored in the linked list's nodes correspond to those of the list lst,
               and appear in the same order as in that list.
               If no list lst is passed as argument, the newly created linked list
               will have 0 length, contain no nodes and its head will point to None. 
        """
        self.length = 0          # current length of the linked list
        self.head = None         # pointer to the first node in the list
        self.last = None         # pointer to the last node in the list
        lst.reverse()            # reverse to ensure elements will appear in same order
        for e in lst :           # add elements of input list lst one by one 
            self.add(e)
            
    def size(self):
        """
        Accessor method which returns the number of nodes contained in this linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.length
    
    def inc_size(self):
        """
        Mutator method to increase the size count of this linked list by one.
        @pre:  -
        @post: 1 has been added to the size counter of the number of nodes contained in this linked list.
        """
        self.length += 1

    def dec_size(self):
        """
        Mutator method to decrease the size count of this linked list by one.
        @pre:  -
        @post: 1 has been substracted from the size counter of the number of nodes contained in this linked list.
        """
        self.length -= 1

    def first(self):
        """
        Accessor method which returns the first node of this linked list.
        @pre:  -
        @post: Returns a reference to the head of this linked list,
               or None if the linked list contains no nodes.
        """
        return self.head
    
    def set_first(self,n):
        """
        Mutator method to reassign the head of this linked list to a new node.
        @pre:  -
        @post: The head of this linked list new refers to node n.
        """
        self.head = n
        
    def add(self, cargo):
        """ 
        Adds a new Node with given cargo to the front of this linked list. 
        @pre:  self is a (possibly empty) LinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented by 1.
               The head of the linked list now points to this new node.
        """
        node = Node(cargo,self.first())
        if self.first() == None :   # when this is the first element being added,
            self.last = node        # set the last pointer to this new node
        self.set_first(node)
        self.inc_size()

    def remove(self):
        """
        Removes the node at the start of the list. Leaves the list intact if already empty. 
        """
        if self.first() is not None:
            self.dec_size()
            self.set_first(self.first().next())
        if self.size() == 0:       # when there are no more elements in the list, after
            self.last = None       # removal, remove the pointer to the last element
    
    def __str__(self):
        """
        Retourne le contenu de cette liste chainée comme un string
        dans le format "[ val_1 ... val_n ]" ou val_i est la valeur
        contenu dans le noeud à la position i de cette liste.
        """
        s = "["
        current = self.first()
        while current is not None:
            s += " " + str(current)
            current = current.next()
        s += "]"
        return s

##############
# Node class #
##############

class Node:

    def __init__(self, cargo=None, next=None):
        """
        Initialises a new Node object.
        @pre:  -
        @post: A new Node object has been initialised.
               A node can contain a cargo and a reference to another node.
               If none of these are given, the node is initialised with
               empty cargo (None) and no reference (None).
        """
        self.cargo = cargo
        self.nxtnode  = next

    def value(self):
        """
        Returns the value of the cargo contained in this node.
        @pre:  -
        @post: Returns the value of the cargo contained in this node, 
               or None if no cargo  was put there.
        """
        return self.cargo

    def next(self):
        """
        Returns the next node to which this node links.
        @pre:  -
        @post: Returns the node to which this node is linked with its 
               next pointer, or None if that pointer is None.
        """
        return self.nxtnode

    def set_next(self,node):
        """
        Sets the next node to which this node links to a new node.
        @pre:  -
        @post: The node to which this node is linked next, 
            has been set to the new node passed as parameter.
            Can also be set to None by passing None as parameter.
        """
        self.nxtnode = node

    def __str__(self):
        """
        Returns a string representation of the cargo of this node.
        @pre:  self is a (possibly empty) Node object.
        @post: Returns a print representation of the cargo contained in this Node.
        """
        return str(self.value())

    def __eq__(self,other):
        """
        Comparator to compare two Node objects by their cargo.
        @pre:  other is a valid object of type Node
        @post: Return True if the cargo contained by this node (self)
               is equal (==) to that contained by the other object.
               Returns False otherwise, or if other is not of type Node.
        """
        if isinstance(other, Node):
            return self.value() == other.value()
        return False
