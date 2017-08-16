#!/usr/bin/env python

from DCList import DCList


class StackList(DCList):
    """ StackList Class
    """

    def __init__(self):
        """ Constructor
        Calls init from DCList
        """
        DCList.__init__(self)

    def push(self, data):
        """ Push an object onto the StackList
        :param data: object to push
        """
        self.insertBefore(data)

    def pop(self):
        """ Pops an object from the StackList
        :return: The top object on the StackList
        """
        tail_data = self.peek()
        self.remove(self.length-1)
        return tail_data

    def peek(self):
        """ Shows the top element of the StackList, without removing it.
        :return: Top object on the StackList
        """
        if self.head is None:
            raise IndexError("Empty StackList")
        return self.tail.data

    def purge(self):
        """ Remove all elements from the StackList
        """
        self.__init__()

    def __len__(self):
        """ Overload.
        :return: The number of elements in the StackList
        """
        return self.length

