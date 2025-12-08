###########################
# OrderedLinkedList class #
###########################

class OrderedLinkedList:
    class Node:
        def __init__(self, data, pre=None, next=None):
            self.data = data
            self.pre = pre
            self.next = next
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
        self.__head = None
        self.__tail = None
        self.__length = 0
            
    def size(self):
        """
        Accessor method which returns the number of nodes contained in this ordered linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this ordered linked list.
        """
        return self.__length
        
    def add(self, cargo):
        """ 
        Adds a new Node with given cargo to the ordered linked list such that the order is maintained
        @pre:  self is a (possibly empty) LinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the ordered linked list in an ordered manner.
               The length counter has been incremented by 1.
        """
        new_node = self.Node(cargo,self.__tail,None)
        self.__tail.next = new_node
        self.__tail = new_node
        if self.__head == None:
            self.__head = self.__tail
        self.__length += 1


    def remove(self, cargo):
        """
        Removes the first node with a given cargo from the list.
        Leaves the list intact if already empty or if a node with that cargo
        doesn't exist.
        """
        if self.__head != None:
            done = False
            if self.__head.data == cargo:
                self.__head == self.__head.next
                self.__head.pre = None
                done = True
            else:
                cur = self.__head
                while cur.next is not None and cur.next.data != cargo:
                    if cur.next.data == cargo:
                        cur.next = cur.next.next
                        cur.next.pre = cur
                        done = True
                    cur = cur.next
            if done:
                self.__length -= 1


