class ToDoListClass:
    def __init__(self, title, category, todolist, owner, last_edit_date):
        self.title = title
        self.category = category
        self.todolist = todolist
        self.owner = owner
        self.last_edit_date = last_edit_date

    def AddOnList(self, selectedlist, last_edit_date):
        selectedlist.append(input("Write: "))
        print("\nAdded on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
        print(selectedlist)
        return selectedlist

    def EditOnList(self, selectedlist, last_edit_date):
        print(selectedlist)
        editedItem = input("Which item you wish to edit (type number): ")
        selectedlist.remove(selectedlist[int(editedItem) - 1])
        selectedlist.append(input("What you wish to rewrite: "))
        print("\nEdited on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
        print(selectedlist)
        return selectedlist

    def DeleteOnList(self, selectedlist, last_edit_date):
        deletedItem = input("Which item you wish to delete (type number): ")
        selectedlist.remove(selectedlist[int(deletedItem) - 1])
        print("\nDeleted on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
        return selectedlist

    def CleanList(self, selectedObj, all_lists, last_edit_date):
        all_lists.remove(selectedObj)
        print("Completed on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
        return all_lists

    # GETTERS N SETTERS
    def get_title(self):
        return self.title

    def get_category(self):
        return self.category

    def get_list(self):
        return self.todolist

    def get_owner(self):
        return self.owner

    def get_last_edit_date(self):
        return self.last_edit_date

    def set_title(self, title):
        self.title = title

    def set_category(self, category):
        self.category = category

    def set_list(self, todolist):
        self.todolist = todolist

    def set_owner(self, owner):
        self.owner = owner

    def set_last_edit_date(self, last_edit_date):
        self.last_edit_date = last_edit_date
