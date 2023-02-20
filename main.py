from datetime import datetime
from ToDoList import ToDoList

def AddOnList(selectedlist):
    selectedlist.append(input("Write: "))
    print(selectedlist)
    return selectedlist

def EditOnList(selectedlist):
    print(selectedlist)
    editedItem = input("Which item you wish to edit (type number): ")
    selectedlist.remove(selectedlist[int(editedItem) - 1])
    selectedlist.append(input("What you wish to rewrite: "))
    print(selectedlist)
    return selectedlist

def DeleteOnList(selectedlist):
    print(selectedlist)
    deletedItem = input("Which item you wish to delete (type number): ")
    selectedlist.remove(selectedlist[int(deletedItem) - 1])
    print(selectedlist)
    return selectedlist



def listActionFunction(action,selectedlist,listNumber,all_lists,all_listnames):
    while True:
        match action:
            case '1':
                AddOnList(selectedlist)
                break
            case '2':
                EditOnList(selectedlist)
                break
            case '3':
                DeleteOnList(selectedlist)
                break
            case '4':
                all_lists.remove(int(listNumber-1))
                all_listnames.remove(int(listNumber-1))
                i = 1
                for item in all_lists:
                    print(str(i) + ". " + all_listnames[i - 1].capitalize() + " - " + str(item))
                    i = i + 1
            case '5':
                break




all_lists=[["run 10km","cook eggs","write code"],["onions","tomatos","cheese","shampoo"]]
all_listnames=["daily routine","market"]

import ToDoList

while True:
    print("\nHello! Welcome to el Todo list!\n - Menu:")
    print("1. Create new list\n2. Show lists\n3. Exit\n")
    user_insert1=input("Type the number of the action you want, please: ")

    match user_insert1:
        case '1':
            title = input("Title: ")
            category  = input("Category: ")
            owner = input("Owner: ")
            last_edit_date = datetime
            todolist = []
            input_string = input("Enter elements of a list separated by comma: ")
            print("\n")
            todolist = input_string.split(", ")
            print(todolist)
            ToDolist_Obj = ToDoList(title, category, todolist, owner, last_edit_date)
            print(ToDolist_Obj)
            break
        case '2':
            if not all_lists: #in case it is empty
                print("There is no available list.")
            else:
                i = 1
                for item in all_lists:
                    print(str(i) + ". "+all_listnames[i-1].capitalize()+ " - " + str(item))
                    i = i + 1
                user_insert2=input("Type the code of the list you want: ")
                print(all_listnames[int(user_insert2)-1].capitalize() + " - " +str(all_lists[int(user_insert2)-1]))
                print("1. Add\n2. Edit list item\n3. Delete list item\n4. Clean list\n5. Exit\n")
                action = input("Type the number of the action you want, please: ")
                listActionFunction(action,all_lists[int(user_insert2)-1],user_insert2,all_lists,all_listnames)






print("\nThank you!")
