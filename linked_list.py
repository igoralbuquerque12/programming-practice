class Node:
    """
    Represents a node in a linked list.

    Attributes:
    value: The value stored in the node.
    next: A pointer to the next node in the list, initially set to None.
    """

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Represents a linked list.

    This class provides basic operations to manipulate a linked list, such as:
    - appending values to the list
    - printing the list
    - removing a node by its value

    Methods:
    append(value): Adds a new node with the given value at the end of the list.
    print_list(): Prints the values of the nodes in the list in the format "value -> value -> ... -> None".
    remove(value): Removes the node with the specified value from the list.
    """

    def __init__(self):
        self.head = None

    def append(self, value) -> bool:
        new_node = Node(value)

        if not self.head:
            self.head= new_node
            return True
        
        current : Node = self.head 

        while current.next:
            current = current.next
                
        current.next = new_node
        return True

    def print_list(self):
        current = self.head

        while current:
            print(current.value, end=' -> ')
            current = current.next

        print("None")

    def remove(self, value) -> bool:
        current = self.head

        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                else:
                    last.next = current.next
                return True

            last = current
            current = current.next

        print('Element was not found')
        return False
        
