import sys

from BillsCategory import BillsCategory
from GymCategory import GymCategory
from WorkCategory import WorkCategory
import datetime


def listActionFunction(action, selectedObj, all_lists, last_edit_date):
    while True:
        match action:
            case '1':
                return selectedObj.AddOnList(selectedObj.todolist,last_edit_date)
                break
            case '2':
                return selectedObj.EditOnList(selectedObj.todolist,last_edit_date)
                break
            case '3':
                return selectedObj.DeleteOnList(selectedObj.todolist,last_edit_date)
                break
            case '4':
                print("\nCleaning "+selectedObj.get_title()+" list: "+str(selectedObj.todolist))
                return selectedObj.CleanList(selectedObj,all_lists,last_edit_date)
                break
            case '5':
                break
def welcomeMenu():
    print("\nHello! Welcome to el Todo list!\n - Menu:")
    print("1. Create new list\n2. Show lists\n0. Exit\n")
    user_insert1 = input("Type the number of the action you want, please: ")
    return user_insert1

def classMatching(name):

    match name:
        case 'Bills':
            deadline=input("Deadline (m/d/y): ")
            amount = input("Amount: ")
            return BillsCategory(name,deadline,amount)
        case 'Work':
            deadline=input("Deadline (m/d/y): ")
            return WorkCategory(name,deadline) #datetime.datetime.strptime(deadline, '%m/%d/%y')
        case 'Gym':
            timecap = input("Time Cap (mins): ")
            cals=input("Calories goal: ")
            return GymCategory( name, timecap, cals)
        case 'Shopping':
            return 'B'
        case 'Plans':
            return 'C'
        case 'Fun':
            return 'C'

def main():
    from ToDoListClass import ToDoListClass
    from Category import Category

    all_lists = [ToDoListClass("Fitness","Gym",["run","squat","v ups"],"Jo",datetime.datetime.strptime("09/19/10 13:55:26", '%m/%d/%y %H:%M:%S')),
                 ToDoListClass("SuperMarket","Shopping",["onions", "tomatos", "cheese", "shampoo"],"Jo",datetime.datetime.strptime("05/03/17 10:23:06", '%m/%d/%y %H:%M:%S'))]

    while True:

        user_insert1 = welcomeMenu()

        match user_insert1:
            case '1':
                title = input("Title: ").capitalize()
                categoryObj=Category(input("Category: ").capitalize())
                owner = input("Owner: ").capitalize()
                last_edit_date = datetime.datetime.now()
                todolist = []
                input_string = input("Enter elements of a list separated by comma: ")
                print("\n")
                for i in input_string.split(", "):
                    todolist.append(i.capitalize())
                    print(i.capitalize())
                    classMatching(categoryObj.get_name())
                todolist_obj = ToDoListClass("\n"+title,categoryObj.get_name() , todolist, owner, last_edit_date)

                #print(categoryObj.priority(categoryObj.get_name()))



                print("\nCreated on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
                print(str(todolist_obj.get_title())+" - "+str(todolist_obj.get_list()))
                all_lists.append(todolist_obj)
            case '2':
                if not all_lists:  # in case it is empty
                    print("There is no available list.")
                else:
                    last_edit_date = datetime.datetime.now()
                    i = 1
                    for obj in all_lists:
                        print(str(i)+". " + obj.get_title()+" - "+str(obj.get_list())+" - "+str(obj.get_last_edit_date().strftime("%x")+" "+obj.get_last_edit_date().strftime("%X")))
                        i = i + 1
                    user_insert2 = input("Type the number of the list you want: ")
                    print(all_lists[int(user_insert2)-1].get_title()+" - "+str(all_lists[int(user_insert2)-1].get_list()))
                    print("\n1. Add\n2. Edit list item\n3. Delete list item\n4. Clean list\n5. Back to Menu\n0. Exit\n")
                    action = input("Type the number of the action you want, please: ")
                    listActionFunction(action, all_lists[int(user_insert2) - 1],  all_lists,last_edit_date)
            case '5':
                welcomeMenu()
            case '0':
                break

    print("\nThank you!")


if __name__ == "__main__":
    main()
