import json
import os

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


    def graph_list(self):
        file = open("list.txt", "w+")
        file.write('digraph G{\n')
        file.write('	rankdir = TB;')
        file.write('	node[shape=record];\n')
        file.write('	graph[ranksep = "1"];\n\n')

        if self.head is None:
            file.write('	root[label="{The Blockchain is empty}"];\n')
        else:
            aux_head = self.head
            while aux_head is not None:
                data = json.loads(aux_head.data)
                file.write('	node{}[label="CLASS: {} \\n TIMESTAMP: {} \\n P.HASH: {} \\n HASH: {}"];\n'.format(data["INDEX"], data["CLASS"], data["TIMESTAMP"], data["PREVIOUSHASH"], data["HASH"]))
                if aux_head.next is not None:
                    next_data = json.loads(aux_head.next.data)
                    file.write('	node{}->node{}[dir=both];\n'.format(data["INDEX"], next_data["INDEX"])) 
                aux_head = aux_head.next

        file.write('\n}')
        file.close()

        os.system("dot -Tpng list.txt -o list.png")
        os.system("list.png")

