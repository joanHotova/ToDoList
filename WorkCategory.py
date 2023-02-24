from Category import Category


class WorkCategory(Category):

    def __init__(self, name, deadline):
        super().__init__(name)
        self.deadline = deadline

 # GETTERS N SETTERS
    def get_deadline(self):
        return self.deadline
    def set_deadline(self, deadline):
        self.deadline = deadline #super().features(self.name)#.split("&")

