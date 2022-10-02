class Stack:

    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        """Accepts an item as a paramater and apeeds it to the end of the list.
        Returns nothing.

        The runtime for this method is 0(1), or constant time, because appending to the
         list happens in constant time
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item for the list, 
        which is also the top item of the Stack 

        The runtime here is constant time, because all it does is return the item on
        the list"""
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """Returns the last item in the list, which is also the item at the top
        of the Stack

        This method runs in constant time because indexing into a list is done in constant time"""

        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the string that is representing the Stack.

        This method runs in constant time because finding the length of the list also happens in constant time"""
        return len(self.items)

    def is_empty(self):
        """Returns a Boolean value describing whether or not the Stack is empty.

        This method runs in constant time because finding the length of the list also happens in constant time"""
        return self.items == []
