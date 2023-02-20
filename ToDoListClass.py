class ToDoListClass:
      def __init__(self, title, category, todolist, owner, last_edit_date):
          self.title=title
          self.category=category
          self.todolist=todolist
          self.owner=owner
          self.last_edit_date=last_edit_date



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