#!/usr/bin/env python

from DCList import DCList


class QueueList(DCList):
    """ QueueList Class
    """

    def __init__(self):
        """ Constructor
        Calls init from DCList
        """
        DCList.__init__(self)

    def push(self, data):
        """ Push an object onto the QueueList
        :param data: object to push
        """
        self.insertBefore(data)

    def pop(self):
        """ Pops an object from the QueueList
        :return: The top object on the QueueList
        """
        
        head_data = self.peek()
        self.remove()
        return head_data

    def peek(self):
        """ Shows the top element of the QueueList, without removing it.
        :return: Top object on the QueueList
        """
        if self.head is None:
            raise IndexError("Empty QueueList")
        return self.head.data

    def purge(self):
        """ Remove all elements from the QueueList
        """
        self.__init__()#tret el self de dins()
     
    def __len__(self):
        """ Overload.
        :return: The number of elements in the QueueList
        """
        return self.length

