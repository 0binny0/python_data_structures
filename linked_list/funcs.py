
import os
from time import sleep

def get_value_to_be_deleted(linked_list):
    cls()
    ll = f"{linked_list}"
    print(f"Linked List: {ll}")
    prompt = "\nProvide the data value of the node to be deleted: "
    try:
        node_data_value = int(input(prompt))
    except ValueError:
        print("\nThe linked list doesn't accept that value.")
        sleep(1.5)
        return
    else:
        if node_data_value not in linked_list:
            print(f"\nNo node exists with a value of {node_data_value}.")
            sleep(1.5)
            return
        return node_data_value

def prompt_list_operation(linked_list):
    current_linked_list = f"{linked_list}"
    operation_set = False
    while True:
        if operation_set:
            print("Linked list: " + current_linked_list)
        while not operation_set:
            print("Linked list: " + current_linked_list)
            print('''
                SET - sets the head node
                APPEND - appends a node to the tail of the list
                INSERT - inserts a node in the middle of the list
                DELETE - deletes a node
                EXIT
            ''')
            operation = input("What operation do you want to perform? ").upper()
            if operation not in ['SET', 'APPEND', 'INSERT', 'DELETE', 'EXIT']:
                '''Wait 1 sec to print'''
                sleep(0.5)
                print("\nInvald operation...")
                '''Wait 1 sec to loop back'''
                sleep(1.5)
                cls()
                '''clear screen'''
            else:
                operation_set = True
                break
        if linked_list.head is None and (operation == "INSERT" or operation == "DELETE"):
                print(f"\nCannot {operation.lower()} a node at this time.")
                data = None
                sleep(1.5)
                break
        else:
            if operation == "SET" or operation == "APPEND" or operation == "INSERT":
                data = get_node_value(linked_list)
                if not data:
                    cls()
                    operation_set = False
                    continue
                else:
                    break
            elif operation == "DELETE":
                data = get_value_to_be_deleted(linked_list)
                break
            else:
                data = None
                break
    return operation, data


def get_node_value(linked_list):
    numbers = [f'{n}' for n in range(1, 10)]
    numbers_available = numbers.copy()
    for i in numbers:
        value = int(i)
        if value in linked_list:
            numbers_available.remove(i)
        continue
    if not numbers_available:
        print("\nNo space to add to the list. Delete a node.")
        sleep(1.5)
        return
    availablity = ' '.join(f"[{n}]" for n in numbers_available)
    prompt = "\nChose from from these numbers to add to the linked list: "
    value = input(prompt + availablity + ": ")
    if value not in numbers_available:
        print("\nInvalid value selected")
        sleep(1)
        return
    else:
        value = int(value)
    return value

def get_replaced_node(linked_list):
    cls()
    ll = f"{linked_list}"
    print(f"Linked List: {ll}")
    prompt = "\nProvide the data value of the node to be inserted: "
    try:
        node_data_value = int(input(prompt))
    except ValueError:
        print("\nThe linked list doesn't accept that value.")
        sleep(1.5)
        cls()
        return
    else:
        if node_data_value not in linked_list:
            print(f"\nNo node exists with a value of {node_data_value}.")
            sleep(1.5)
            cls()
            return
        return node_data_value



def cls():
    os.system('cls' if os.name=='nt' else 'clear')
