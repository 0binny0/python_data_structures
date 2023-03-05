
import os
from time import sleep

def prompt_list_operation(linked_list):
    current_linked_list = f"{linked_list}"
    operation_set = False
    while True:
        print("Linked List: " + current_linked_list)
        while not operation_set:
            print('''
                SET - sets the head node
                APPEND - appends a node to the tail of the list
                INSERT - inserts a node in the middle of the list
                DELETE - deletes a node
                EXIT
            ''')
            user_input = input("What operation do you want to perform? ").upper()
            if operation not in ['SET', 'APPEND', 'INSERT', 'DELETE', 'EXIT']:
                '''Wait 1 sec to print'''
                sleep(1)
                print("\nInvald operation...")
                '''Wait 1 sec to loop back'''
                cls()
                '''clear screen'''
            else:
                operation_set = True
                break
        if operation != EXIT:
                data = get_node_value(linked_list)
                if not data:
                    if operation == "APPEND":
                        break
                    else:
                        continue
                else:
                    break
        else:
            data = None
    cls()
    return operation, data


def get_node_value(linked_list):
    numbers = [f'{n}' for n in range(1, 10)]
    numbers_available = numbers
    for i in numbers:
        value = int(i)
        if value in linked_list:
            numbers_available.remove(i)
    if not numbers_available:
        sleep(1)
        print("No space to add to the list. Delete a node.")
        return
    availablity = ' '.join(f"[{n}]" for n in numbers_available)
    prompt = "\nChose from from these numbers to add to the linked list: "
    value = input(prompt + availablity)
    if value not in numbers_available:
        sleep(1)
        print("\n\Invalid value selected.")
        return
    else:
        value = int(value)
    return value


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
