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
        which is also the top item of the Stack """
        return self.items.pop()

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass
