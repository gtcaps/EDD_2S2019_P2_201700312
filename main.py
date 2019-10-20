from list import DoublyLinkedList
from methods import *
from pathlib import Path
from thread_client import Thread_Client
import sys



blocks_list = DoublyLinkedList()
selected_block = None
waiting_block = None


thread_client = Thread_Client(waiting_block, blocks_list)



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
            select_block(blocks_list.head)
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
        waiting_block = file_data
        thread_client.send_message(file_data)
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
        

def select_block(block):
    if blocks_list is None:
        print("     No existe ningun bloque en la lista")
    else:
        try:
            data_aux = json.loads(block.data)
            selected = int(input(""" 
            -------------- SELECT BLOCK --------------
            INDEX: {}
            CLASS: {}
        
            1. SELECT THIS BLOCK
            2. NEXT BLOCK
            3. PREVIOUS BLOCK
            4. BACK TO MAIN MENU
            ------------------------------------------
            SELECT A OPTION: 
            """.format(data_aux["INDEX"], data_aux["CLASS"])))

            if selected is 1:
                print("bloque seleccionado + " + str(data_aux["INDEX"]))
            elif selected is 2 and block.next is not None:
                select_block(block.next) 
            elif selected is 3 and block.back is not None:
                select_block(block.back) 
            elif selected is 4:
                return 0
            else:
                select_block(block)
        except:
            select_block(block)

        

main_menu()