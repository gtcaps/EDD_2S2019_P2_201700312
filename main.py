from list import DoublyLinkedList
from methods import *


my_list = DoublyLinkedList()
my_list.add(data_to_json('file', my_list))
my_list.add(data_to_json('file2', my_list))
my_data = data_to_json('file2', my_list)
#print(verify_json_string(my_data))
#generate_avl(my_data)

my_list.graph_list()

#my_list.print()
