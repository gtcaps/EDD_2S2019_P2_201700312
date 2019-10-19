import os

class Node:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = name
        self.balance = 0
        self.right = None
        self.left = None


class AVL:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def addRoot(self, id, name):
        self.root = Node(id, name)
        self.root.balance = self.maxHeight(
            self.root.right) - self.maxHeight(self.root.left)

    def addNode(self, id, name, node):

        if node is None:
            return Node(id, name)

        if id < node.id:
            node.left = self.addNode(id, name, node.left)
        
        elif id > node.id:
            node.right = self.addNode(id, name, node.right)

        node_balance = self.maxHeight(node.right) - self.maxHeight(node.left)

        
        if node_balance >= 2 and node.right.balance > 0:
            node = self.left_rotation(node)           
        elif node_balance <= -2 and node.left.balance < 0:
            node = self.right_rotation(node)
        elif node_balance >= 2 and node.right.balance < 0:
            node = self.left_double_rotation(node)    
        elif node_balance <= -2 and node.left.balance > 0:
            node = self.right_double_rotation(node)
        
            
        node.balance = node_balance
        
        return node

    def in_order_traversal(self, node):
        if self.isEmpty():
            print("BST is empty")
        else:
            if node is not None:
                self.in_order_traversal(node.left)
                print(str(node.id) + " --- " + str(node.balance))
                self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if self.isEmpty():
            print("BST is empty")
        else:
            if node is not None:
                print(str(node.id) + " --- " + str(node.balance))
                self.pre_order_traversal(node.left)
                self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if self.isEmpty():
            print("BST is empty")
        else:
            if node is not None:
                self.post_order_traversal(node.left)
                self.post_order_traversal(node.right)
                print(str(node.id) + " --- " + str(node.balance))

    def maxHeight(self, node):
        if node is None:
            return 0
        else:
            leftD = self.maxHeight(node.left)
            rightD = self.maxHeight(node.right)
            return leftD + 1 if leftD > rightD else rightD + 1

    def left_rotation(self, node):
        new_node = Node(node.id, node.name)
        new_node.right = node.right.left
        new_node.left = node.left 
        node = node.right
        node.left = new_node
        return node

    def right_rotation(self, node):
        new_node = Node(node.id, node.name)
        new_node.left = node.left.right
        new_node.right = node.right 
        node = node.left
        node.right = new_node
        return node

    def left_double_rotation(self, node):
        aux_node = node
        aux_node_r = node.right.left.left
        aux_node_2 = node.right.left.right      
        node = node.right.left
        node.right = aux_node.right
        node.right.left = None
        node.left = aux_node
        node.left.right = aux_node_r
        node.right.left = aux_node_2  
        return node

    def right_double_rotation(self, node):
        aux_node = node
        aux_node_l = node.left.right.right
        aux_node_2 = node.left.right.left
        node = node.left.right
        node.left = aux_node.left
        node.left.right = None
        node.right = aux_node
        node.right.left = aux_node_l
        node.left.right = aux_node_2
        return node

    def add(self, id, name):
        if self.isEmpty():
            self.addRoot(id, name)
        else:
            self.root = self.addNode(id, name, self.root)

    def in_order(self):
        self.in_order_traversal(self.root)

    def pre_order(self):
        self.pre_order_traversal(self.root)

    def post_order(self):
        self.post_order_traversal(self.root)

    def graph_tree(self, file, node):
        
        if node is not None:

            alumn_id = str(node.id).replace('-','_')
            alumn_name = node.name
            alumn_height = self.maxHeight(node) - 1
            alumn_balance = self.maxHeight(node.right) - self.maxHeight(node.left)         
            file.write('	nodo_{0}[label="<l>|Carne: {0} \\n Nombre: {1} \\n Altura: {2} \\n FE: {3} |<r>"];\n'.format(alumn_id, alumn_name, alumn_height, alumn_balance))

            if node.left is not None:
                file.write('	nodo_{}:l->nodo_{};\n'.format(str(node.id).replace('-','_'),str(node.left.id).replace('-','_')))

            if node.right is not None:
                file.write('	nodo_{}:r->nodo_{};\n'.format(str(node.id).replace('-','_'),str(node.right.id).replace('-','_')))

            self.graph_tree(file, node.left)
            self.graph_tree(file, node.right)
        
    def graph_inorder(self, alumns_list , node):
        if node is not None:
            alumn_id = str(node.id).replace('-','_')
            alumn_name = node.name
            alumn = '{} \\n {}'.format(alumn_id, alumn_name)

            self.graph_inorder(alumns_list, node.left)
            alumns_list.append(alumn)
            self.graph_inorder(alumns_list, node.right)
    
    def graph_preorder(self, alumns_list , node):
        if node is not None:
            alumn_id = str(node.id).replace('-','_')
            alumn_name = node.name
            alumn = '{} \\n {}'.format(alumn_id, alumn_name)

            alumns_list.append(alumn)
            self.graph_preorder(alumns_list, node.left)
            self.graph_preorder(alumns_list, node.right)
        
    def graph_postorder(self, alumns_list , node):
        if node is not None:
            alumn_id = str(node.id).replace('-','_')
            alumn_name = node.name
            alumn = '{} \\n {}'.format(alumn_id, alumn_name)

            self.graph_postorder(alumns_list, node.left)
            self.graph_postorder(alumns_list, node.right)
            alumns_list.append(alumn)

    def graph_list(self, file, alumns_list, title):
        for i in range(len(alumns_list)):
            file.write('	nodo_{}[label="{}"];\n'.format(str(i), alumns_list[i]))
            file.write('    nodo_{}->nodo_{};\n'.format(str(i), str(i + 1))) if i is not len(alumns_list) - 1 else ''

        file.write('    label="{}";\n'.format(title))

    def graph(self, graph_type):
        f = open("avl.txt", "w+")
        f.write('digraph G{\n')
        f.write('	rankdir = TB;\n' if graph_type is 'full' else '	rankdir = LR;\n')
        f.write('	node[shape=record];\n')
        f.write('	graph[ranksep = "1"];\n\n')

        if graph_type is 'full':
            self.graph_tree(f, self.root)
        elif graph_type is 'inorder':
            alumns_list = []
            self.graph_inorder(alumns_list, self.root)
            self.graph_list(f, alumns_list, 'In Order')
        elif graph_type is 'preorder':
            alumns_list = []
            self.graph_preorder(alumns_list, self.root)
            self.graph_list(f, alumns_list, 'Pre Order')
        elif graph_type is 'postorder':
            alumns_list = []
            self.graph_postorder(alumns_list, self.root)
            self.graph_list(f, alumns_list, 'Post Order')

        f.write('\n}')
        f.close()

        os.system("dot -Tpng avl.txt -o avl.png")
        os.system("avl.png")
