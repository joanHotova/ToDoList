
def listActionFunction(action, selectedObj, listNumber, all_lists):
    while True:
        match action:
            case '1':
                return selectedObj.AddOnList(selectedObj.todolist)
                break
            case '2':
                return selectedObj.EditOnList(selectedObj.todolist)
                break
            case '3':
                return selectedObj.DeleteOnList(selectedObj.todolist)
                break
            case '4':
                break
            case '5':
                break


def main():
    from ToDoListClass import ToDoListClass
    from datetime import datetime

    all_lists = [ToDoListClass("Fitness","Life",["run","squat","v ups"],"Jo",""),
                 ToDoListClass("SuperMarket","Outcomes",["onions", "tomatos", "cheese", "shampoo"],"Jo","")]

    while True:
        print("\nHello! Welcome to el Todo list!\n - Menu:")
        print("1. Create new list\n2. Show lists\n3. Exit\n")
        user_insert1 = input("Type the number of the action you want, please: ")

        match user_insert1:
            case '1':
                title = input("Title: ").capitalize()
                category = input("Category: ").capitalize()
                owner = input("Owner: ").capitalize()
                last_edit_date = datetime
                todolist = []
                input_string = input("Enter elements of a list separated by comma: ")
                print("\n")
                todolist = input_string.split(", ").capitalize()
                print(todolist)
                todolist_obj = ToDoListClass(title, category, todolist, owner, last_edit_date)
                break
            case '2':
                if not all_lists:  # in case it is empty
                    print("There is no available list.")
                else:
                    i = 1
                    for obj in all_lists:
                        print(str(i)+". " + obj.get_title()+" - "+str(obj.get_list()))
                        i = i + 1
                    user_insert2 = input("Type the number of the list you want: ")
                    print(all_lists[int(user_insert2)-1].get_title()+" - "+str(all_lists[int(user_insert2)-1].get_list()))
                    print("\n1. Add\n2. Edit list item\n3. Delete list item\n4. Clean list\n5. Exit\n")
                    action = input("Type the number of the action you want, please: ")
                    listActionFunction(action, all_lists[int(user_insert2) - 1], user_insert2, all_lists)

    print("\nThank you!")


if __name__ == "__main__":
    main()
