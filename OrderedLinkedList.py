###########################
# OrderedLinkedList class #
###########################

class OrderedLinkedList:
    
    def __init__(self, lst=[]):
        """
        Initialises a new linked list object, with a given list of elements lst.
        @pre:  -
        @post: A new ordered linked list object has been initialised.
               Its length is equal to the number of elements in lst.
               The data elements stored in the linked list's nodes correspond to those of the list lst,
               and appear in the same order as in that list.
               If no list lst is passed as argument, the newly created linked list
               will have 0 length, contain no nodes and its head will point to None. 
        """
        pass
            
    def size(self):
        """
        Accessor method which returns the number of nodes contained in this ordered linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this ordered linked list.
        """
        pass
        
    def add(self, cargo):
        """ 
        Adds a new Node with given cargo to the ordered linked list such that the order is maintained
        @pre:  self is a (possibly empty) LinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the ordered linked list in an ordered manner.
               The length counter has been incremented by 1.
        """
        pass

    def remove(self, cargo):
        """
        Removes the first node with a given cargo from the list.
        Leaves the list intact if already empty or if a node with that cargo
        doesn't exist.
        """
        pass


