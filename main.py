from list import DoublyLinkedList
from methods import *
from pathlib import Path
import sys


blocks_list = DoublyLinkedList()
selected_block = None


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
        4. EXIT
        ---------------------------------------------
        SELECT A OPTION: 
        """))

        if option is 1:
            insert_menu()
        elif option is 2:
            print("SELECCIONASTE 2")
        elif option is 3:
            reports_menu()
        elif option is 4:
            return 0
        else:
            main_menu()

        main_menu()
    except:
        main_menu()
    

def insert_menu():
    file_name = input("""
    -------------- INSERT BLOCKCHAIN --------------
    INSERT THE NAME OF THE FILE (.CSV): 
    """)

    file_path = Path('./blocks/{}.csv'.format(file_name))

    if file_path.is_file():
        file_data = data_to_json(file_name, blocks_list)
        print(file_data)
    else:
        print("\n\n    [ERROR] EL ARCHIVO {}.csv QUE INTENTAS CARGAR NO EXISTE".format(file_name))

    

def reports_menu():
    try:
        report_option = int(input(""" 
        -------------- REPORTS --------------
        1. BLOCKHAIN REPORT
        2. TREE REPORTS
        3. BACK TO MENU
        --------------------------------------
        SELECT A OPTION: 
        """))

        if report_option is 1:
            blocks_list.graph_list()
        elif report_option is 2:
            selected_block_menu()
        elif report_option is 3:
            return 0
        else:
            reports_menu()
        reports_menu()
    except:
        reports_menu()


def selected_block_menu():
    if selected_block is None:
        print("\n\n    Debes seleccionar primero un bloque")
    else:
        try:
            block_menu_option = int(input(""" 
            -------------- TREE REPORTS --------------
            1. FULL TREE
            2. INORDER TRAVERSAL
            3. PREORDER TRAVERSAL
            4. POSTORDER TRAVERSAL
            5. BACK TO REPORTS MENU
            --------------------------------------
            SELECT A OPTION:
            """))

            if block_menu_option is 1:
                #graficar el arbol completo
                print('full tree')
            elif block_menu_option is 2:
                #graficar el arbol con el recorrido en orden
                print('inorder traversal')
            elif block_menu_option is 3:
                #graficar el arbol con el recorrido en pre orden
                print('preorder traversal')
            elif block_menu_option is 4:
                #graficar el arbol con el recorrido en post orden
                print('postorder traversal')
            elif block_menu_option is 5:
                return 0
            else:
                selected_block_menu()
            selected_block_menu()
        except:
            selected_block_menu()
        

main_menu()