import json

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.back = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.length += 1
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.back = self.tail
            self.tail = new_node
            self.length += 1

    def print(self):
        if self.head is None:
            print("The list is empty")
        else:
            self.print_recursive(self.head)

    def print_recursive(self, node):
        if node is not None:
            print(node.data)
            self.print_recursive(node.next)


    def get_last_hash(self):
        if self.head is None:
            return '0000'
        else:
            hash = json.loads(self.tail.data)
            return hash["HASH"]



