from list import DoublyLinkedList
from methods import *
import sys

'''
my_list = DoublyLinkedList()
my_list.add(data_to_json('file', my_list))
my_list.add(data_to_json('file2', my_list))
my_data = data_to_json('file2', my_list)
#print(verify_json_string(my_data))
#generate_avl(my_data)

my_list.graph_list()

#my_list.print()
'''


def main_menu():

    try:

        option = int(input(""" 
        -------------- BLOCKCHAIN MENU --------------
        1. INSERT BLOCK
        2. SELECT BLOCK
        3. REPORTS
        ---------------------------------------------
        SELECT A OPTION: 
        """))

        if option is 1:
            print("SELECCIONASTE 1")
        elif option is 2:
            print("SELECCIONASTE 2")
        elif option is 3:
            print("SELECCIONASTE 3")
        else:
            main_menu()
    except:
        main_menu()
    

main_menu()