from Category import Category


class ShoppingCategory(Category):

    def __init__(self, name, budget):
        super().__init__(name)
        self.budget=budget

 # GETTERS N SETTERS
    def get_budget(self):
        return self.budget
    def set_budget(self, budget):
        self.budget = budget
