class Stack:
    def __init__(self, capacity):
        """
        Constructor for the Stack class.

        Args:
            capacity: Maximum capacity of the stack.
        """
        self.top = -1                  # Initialize top index to -1 (empty stack)
        self.capacity = capacity        # Set the maximum capacity of the stack
        self.itens = list()            # Initialize an empty list to represent the stack
        self.size = 0                  # Initialize the size of the stack to 0

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def isFull(self):
        """
        Check if the stack is full.

        Returns:
            True if the stack is full, False otherwise.
        """
        return self.size == self.capacity

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to be added to the stack.

        Returns:
            True if the item was successfully added, False if the stack is full.
        """
        if not self.isFull():
            self.top += 1
            self.itens.append(item)  # Append the item to the list
            self.size += 1
            return True
        else:
            return False

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        Returns:
            The item removed from the top of the stack.
        """
        if not self.isEmpty():
            oldTop = self.itens.pop()  # Remove and return the last item from the list
            self.top -= 1
            self.size -= 1
            return oldTop

    def peek(self):
        """
        Peek at the item on the top of the stack without removing it.

        Returns:
            The item on the top of the stack.
        """
        if not self.isEmpty():
            return self.itens[self.top]

    def showStack(self):
        """
        Display the elements of the stack.

        Prints a visual representation of the stack elements.
        """
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack Elements:")
            for item in reversed(self.itens):
                print("|", item, "|")
            print("  ---")

    def clean(self):
        """
        Remove all elements from the stack.
        """
        if not self.isEmpty():
            for item in range(self.size):
                self.pop()
