Static Stack Implementation in Python
This Python implementation provides a simple stack data structure. A stack follows the Last In, First Out (LIFO) principle, where the last element added is the first one to be removed.

Stack Class
Constructor (__init__):
Parameters:
capacity: Maximum capacity of the stack.
Attributes:
top: Index of the top element (initialized to -1 for an empty stack).
capacity: Maximum capacity of the stack.
itens: List to represent the stack.
size: Current size of the stack.
isEmpty Method:
Returns:
True if the stack is empty, False otherwise.
isFull Method:
Returns:
True if the stack is full, False otherwise.
push Method:
Parameters:
item: The item to be added to the stack.
Returns:
True if the item was successfully added, False if the stack is full.
pop Method:
Returns:
The item removed from the top of the stack.
peek Method:
Returns:
The item on the top of the stack without removing it.
showStack Method:
Prints:
A visual representation of the stack elements.
clean Method:
Removes:
All elements from the stack.
Usage
Import the Stack class into your Python script or application.
python
Copy code
from stack import Stack
Create an instance of the Stack class with a specified capacity.
python
Copy code
my_stack = Stack(5)  # Example capacity of 5
Use the various methods provided by the class to manipulate the stack.
python
Copy code
my_stack.push(42)
my_stack.push(17)
my_stack.showStack()
popped_item = my_stack.pop()
print(f"Popped item: {popped_item}")
Feel free to incorporate this stack implementation into your projects and modify it based on your specific requirements. If you encounter any issues or have suggestions for improvements, please feel free to contribute.
