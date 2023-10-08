class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert(self, data, position):
        new_node = Node(data)
        if position < 0:
            print("Invalid position")
            return
        elif position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current:
                if count == position:
                    new_node.prev = current.prev
                    new_node.next = current
                    if current.prev:
                        current.prev.next = new_node
                    current.prev = new_node
                    return
                count += 1
                current = current.next
            print("Invalid position")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Example usage:
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.insert(0, 0)  # Insert 0 at position 0
dllist.insert(4, 2)  # Insert 4 at position 2
dllist.display()
