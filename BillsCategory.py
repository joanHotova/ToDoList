from Category import Category


class BillsCategory(Category):
    def __init__(self, name, deadline, amount):
        super().__init__(name)
        self.deadline = deadline
        self.amount = amount

 # GETTERS N SETTERS

    def get_deadline(self):
        return self.deadline

    def set_deadline(self, deadline):
        self.deadline = deadline  # super().features(self.name)#.split("&")
    def get_amount(self):
        return self.amount
    def set_amount(self, amount):
        self.amount = amount
